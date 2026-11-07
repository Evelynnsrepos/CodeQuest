---
title: The context budget and prompt caching
minutes: 25
xp: 45
hint: tokens: return len(text) // 4
hint: tokens_left: used = 0, then for part in parts: and inside it used = used + part. Then return window - used - reserve
hint: request_cost: paid_tokens = cached * cache_factor + new, then return paid_tokens * price_per_million / 1_000_000
---
# Everything is re-sent, every time

⏱️ About 25 minutes

> **Warm-up:** you've chatted with an agent for an hour. On your next message, how much text does the model actually receive?

**In one sentence:** the model has no memory between requests, so the harness re-sends system prompt + tool descriptions + memory files + the whole history every time, and it all has to fit in the context window.

## 🪜 Plain words

Each request = **system prompt** + **tool descriptions** + **memory files** (CLAUDE.md…) + **history** (your messages, replies, tool results) + room for the **answer**.

When that gets near the window size, the harness **compacts**: it replaces old history with a summary. Details can get lost, which is why anything important belongs in a memory file.

**Prompt caching:** the unchanged **start** of the prompt can be reused from the provider's cache, so it is much cheaper (with Anthropic's API, cache reads cost a tenth of the normal input price). The catch: the **first** request that writes those tokens into the cache costs a bit **more** than normal (with Anthropic, 1.25× the input price for the 5-minute cache, 2× for the 1-hour cache), and the cache expires if it isn't reused. So caching pays off from the second request on. That's why system prompts and memory files are cheap after the first request, and why changing something near the **top** of the prompt is expensive: everything after it must be re-read.

## 🪜 With numbers

Window 200,000 tokens. System 3,000 + tools 12,000 + memory 2,000 + history 150,000 = 167,000. Keep 20,000 for the answer → 187,000 used, **13,000 left** before compaction.

Cost with caching (price 3 $ per million input tokens, cache reads at 0.1×): a request with 160,000 cached tokens and 2,000 new ones = 160,000 × 0.3 + 2,000 × 3 = 48,000 + 6,000 → **0.054 $**, instead of 0.486 $ without caching.

## 🔬 Take the formula apart

<div class="formula"><span class="k1">left</span> = <span class="k2">window</span> − ( <span class="k3">system + tools + memory + history</span> ) − <span class="k4">reserve</span></div>

| Piece | Means | Example |
|---|---|---|
| <span class="k2">window</span> | the model's maximum context | 200,000 |
| <span class="k3">system + tools + memory + history</span> | everything re-sent | 167,000 |
| <span class="k4">reserve</span> | room kept for the answer | 20,000 |
| <span class="k1">left</span> | how much more you can add | 13,000 |

<div class="formula"><span class="k5">cost</span> = ( <span class="k6">cached</span> × 0.1 + <span class="k3">new</span> ) × price per token</div>

## 🔀 What if it were different?

<div class="wrong"><b>Forget the reserve</b>: the prompt fits exactly, the answer gets cut off after a few tokens.</div>
<div class="wrong"><b>Put the current date at the very top of the system prompt</b>: it changes every day, so the cache breaks for everything after it every day.</div>
<div class="wrong"><b>40 MCP tools installed "just in case"</b>: each tool description costs tokens on every single request, and small models get confused past 10–20 tools.</div>
<div class="right">stable things first (cacheable), only the tools you need, a reserve for the answer ✓</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `len(text)` | "length of text" | how many characters: `len("hello")` is `5` |
| `a // b` | "a floor-divided by b" | divides and **throws away** the part after the dot: `27 // 4` is `6` (27 / 4 = 6.75) |
| `used = 0` then `used = used + part` | "used becomes used plus part" | a **running total**: start at 0, add one number each round |
| `a * b / c` | | times and divide, done left to right |
| `1_000_000` | "one million" | Python lets you put `_` in big numbers so you can read them. It's the same as `1000000`. |

### 👀 Worked example: a pocket-money budget

```python
def money_left(start, spent, savings):
    used = 0
    for item in spent:
        used = used + item
    return start - used - savings

print(money_left(50, [12, 8, 5], 10))
```

1. `used` starts at `0`.
2. Round 1: `used = 0 + 12` → 12. Round 2: `12 + 8` → 20. Round 3: `20 + 5` → 25.
3. `50 - 25 - 10` = **15**.

`tokens_left` is the same: the window is the start money, the parts are what's spent, `reserve` is what you keep free for the answer.

And the cost with numbers: 160,000 cached tokens, 2,000 new, $3 per million, cache factor 0.1:

1. `160000 * 0.1` = 16,000. Cached tokens cost a tenth, so they count as 16,000 normal ones.
2. `16000 + 2000` = 18,000 tokens you pay full price for.
3. `18000 * 3 / 1_000_000` = **0.054** dollars.

## 🎯 Your quest

1. `tokens(text)`: rough estimate, `len(text) // 4` (about 4 characters per token in English).
2. `tokens_left(window, parts, reserve)`: `parts` is a list of token counts.
3. `request_cost(cached, new, price_per_million, cache_factor=0.1)`: in dollars.

Lines to type, one function at a time (each replaces that function's `return` line):

`tokens`:

1. `return len(text) // 4`

`tokens_left`:

1. `used = 0`
2. `for part in parts:`
3. `    used = used + part`
4. `return window - used - reserve`

`request_cost`:

1. `paid_tokens = cached * cache_factor + new`
2. `return paid_tokens * price_per_million / 1_000_000`

**Remember:** the model sees only what's re-sent; keep the stable part at the top.

## Review

<details><summary>Which layer decides what goes into the context?</summary>The harness.</details>
