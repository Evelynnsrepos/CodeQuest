---
title: Tracking cost and latency
xp: 55
---
# What does one answer cost, and how long does it take?

> **Warm-up:** your app's average response time is 1.2 seconds. Is everyone happy?

Not necessarily. Averages hide the slow tail: if 1 request in 20 takes 15 seconds, those users leave. Track **percentiles**:

- **p50** (median): the typical request.
- **p95**: 95% of requests are faster than this. The number to watch.
- **p99**: the worst 1%.

**Nearest-rank percentile:** sort the values; the p-th percentile is the value at position ⌈p/100 · n⌉ (counting from 1).

**Cost** per call = input tokens × input price + output tokens × output price (prices per million tokens; LLMs 9 lesson 02). Sum it per day, per user and per feature, and set an **alert** before a bug or an abuser burns your budget. Local models cost electricity and hardware instead of per token, but latency still matters.

## Your quest

`PRICES` maps model → `(input_price, output_price)` per million tokens.

1. `percentile(values, p)`: nearest-rank, as above.
2. `Tracker.record(model, tokens_in, tokens_out, ms)` stores a call; `Tracker.cost()` is the total in dollars; `Tracker.cost_by_model()` a dict model → dollars; `Tracker.latency()` a dict `{"p50": ..., "p95": ..., "p99": ...}` over all calls.
3. `Tracker.over_budget(limit)`: `True` if the total cost is above `limit`.

**Remember:** watch p95, not the average; know your cost per call.

## Review

<details><summary>How does a token bucket allow bursts but limit the average?</summary>It holds up to capacity tokens for bursts, and refills at a fixed rate.</details>
