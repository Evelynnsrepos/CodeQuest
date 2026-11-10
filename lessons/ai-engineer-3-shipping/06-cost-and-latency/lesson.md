---
title: Tracking cost and latency
minutes: 40
xp: 55
hint: percentile: s = sorted(values), rank = math.ceil(p / 100 * len(s)), at least 1, then return s[rank - 1]
hint: record: price_in, price_out = self.prices[model], cost = (tokens_in * price_in + tokens_out * price_out) / 1_000_000, then append a dict
hint: cost: a running total over self.calls. latency: collect every c["ms"], then a dict with percentile(ms, 50), 95 and 99
hint: over_budget: return self.cost() > limit
---
# What does one answer cost, and how long does it take?

⏱️ About 40 minutes

> **Warm-up:** your app's average response time is 1.2 seconds. Is everyone happy?

Not necessarily. Averages hide the slow tail: if 1 request in 20 takes 15 seconds, those users leave. Track **percentiles**:

- **p50** (median): the typical request.
- **p95**: 95% of requests are faster than this. The number to watch.
- **p99**: the worst 1%.

**Nearest-rank percentile:** sort the values; the p-th percentile is the value at position ⌈p/100 · n⌉ (counting from 1).

**Cost** per call = input tokens × input price + output tokens × output price (prices per million tokens; LLMs 9 lesson 02). Sum it per day, per user and per feature, and set an **alert** before a bug or an abuser burns your budget. Local models cost electricity and hardware instead of per token, but latency still matters.

## 🧮 Worked example

Ten response times in milliseconds, already sorted:

80, 85, 90, 95, **100**, 110, 120, 130, 300, **1500**

- **average** = 2,610 ÷ 10 = **261 ms**, which describes nobody
- **p50**: position ⌈0.50 · 10⌉ = 5 → **100 ms**, what a typical user gets
- **p95**: position ⌈0.95 · 10⌉ = ⌈9.5⌉ = 10 → **1500 ms**, what the unlucky ones get

**Cost** of one call with 2,000 input and 500 output tokens at $3 and $15 per million: 2,000 × 3 / 1,000,000 + 500 × 15 / 1,000,000 = 0.006 + 0.0075 = **$0.0135**.

The sign `⌈ ⌉` means **round up** to the next whole number ("ceiling"): ⌈9.5⌉ = 10, ⌈5⌉ = 5. In Python: `math.ceil(9.5)`. The `p` in p50 and p95 stands for **percentile**: p95 is the time that 95% of the calls are faster than.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `sorted(values)` | | a new list, smallest first |
| `math.ceil(p / 100 * len(s))` | | the rank: for p = 95 and 10 values, ⌈9.5⌉ = 10 |
| `s[rank - 1]` | | ranks count from 1, list positions from 0 |
| `price_in, price_out = self.prices[model]` | | the two prices of that model |
| `1_000_000` | | one million (the `_` is just for reading) |
| `out.get(c["model"], 0) + c["cost"]` | | the model's total so far, plus this call |
| `self.cost() > limit` | | `True` or `False` directly |

## 🎯 Your quest

`PRICES` maps model → `(input_price, output_price)` per million tokens.

1. `percentile(values, p)`: nearest-rank, as above.
2. `Tracker.record(model, tokens_in, tokens_out, ms)` stores a call; `Tracker.cost()` is the total in dollars; `Tracker.cost_by_model()` a dict model → dollars; `Tracker.latency()` a dict `{"p50": ..., "p95": ..., "p99": ...}` over all calls.
3. `Tracker.over_budget(limit)`: `True` if the total cost is above `limit`.

**Part 1:** `percentile`. Replace `return 0` with:

1. `s = sorted(values)`
2. `rank = math.ceil(p / 100 * len(s))`
3. `if rank < 1:`
4. `    rank = 1`
5. `return s[rank - 1]`

**Part 2:** the `Tracker` methods (8 spaces, inside the class). `record`: replace `pass` with:

1. `price_in, price_out = self.prices[model]`
2. `cost = (tokens_in * price_in + tokens_out * price_out) / 1_000_000`
3. `self.calls.append({"model": model, "ms": ms, "cost": cost})`

`cost`: replace `return 0.0` with:

1. `total = 0.0`
2. `for c in self.calls:`
3. `    total = total + c["cost"]`
4. `return total`

`cost_by_model`: replace `return {}` with:

1. `out = {}`
2. `for c in self.calls:`
3. `    out[c["model"]] = out.get(c["model"], 0) + c["cost"]`
4. `return out`

`latency`: replace `return {}` with:

1. `ms = []`
2. `for c in self.calls:`
3. `    ms.append(c["ms"])`
4. `return {"p50": percentile(ms, 50), "p95": percentile(ms, 95), "p99": percentile(ms, 99)}`

**Part 3:** `over_budget`. Replace `return False` with:

1. `return self.cost() > limit`

**Remember:** watch p95, not the average; know your cost per call.

## Review

<details><summary>How does a token bucket allow bursts but limit the average?</summary>It holds up to capacity tokens for bursts, and refills at a fixed rate.</details>
