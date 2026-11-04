---
title: The context budget and prompt caching
xp: 45
---
# Everything is re-sent, every time

> **Warm-up:** you've chatted with an agent for an hour. On your next message, how much text does the model actually receive?

**In one sentence:** the model has no memory between requests, so the harness re-sends system prompt + tool descriptions + memory files + the whole history every time, and it all has to fit in the context window.

## 🪜 Plain words

Each request = **system prompt** + **tool descriptions** + **memory files** (CLAUDE.md…) + **history** (your messages, replies, tool results) + room for the **answer**.

When that gets near the window size, the harness **compacts**: it replaces old history with a summary. Details can get lost, which is why anything important belongs in a memory file.

**Prompt caching:** the unchanged **start** of the prompt can be reused from the provider's cache, so it is much cheaper (with Anthropic's API, cache reads cost a tenth of the normal input price). That's why system prompts and memory files are cheap after the first request, and why changing something near the **top** of the prompt is expensive: everything after it must be re-read.

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

## 🎯 Your quest

1. `tokens(text)`: rough estimate, `len(text) // 4` (about 4 characters per token in English).
2. `tokens_left(window, parts, reserve)`: `parts` is a list of token counts.
3. `request_cost(cached, new, price_per_million, cache_factor=0.1)`: in dollars.

**Remember:** the model sees only what's re-sent; keep the stable part at the top.

## Review

<details><summary>Which layer decides what goes into the context?</summary>The harness.</details>
