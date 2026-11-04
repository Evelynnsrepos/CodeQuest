---
title: Batches for one GPU
xp: 30
---
# Don't send 500 items to one graphics card at once

⏱️ About 12 minutes · two small functions

> **Warm-up:** 600 emails go into an Ollama node. Your GPU can answer about 2 at once, 4 seconds each. Roughly how long will it take, and what happens if n8n fires all 600 at once?

**In one sentence:** with a local model your GPU is the bottleneck, so feed it items in **batches** (the *Loop Over Items* node), turn on **Retry On Fail**, and estimate the run time before you start.

## 🪜 The n8n settings

- **Loop Over Items** (also called Split in Batches): passes items on in groups of a size you choose, and loops until all are done.
- Each node's **Settings** tab: **Retry On Fail**, **Max Tries**, **Wait Between Tries (ms)**. Good for a model that's still loading.
- **Timeout** in the workflow settings, so a stuck run ends.

## 🪜 Run-time math, one step at a time

**Step 1. Rounds.** If the GPU handles `parallel` requests at once, the items go through in rounds. The number of rounds is items ÷ parallel, rounded **up** (the last round may be half full):

`rounds = ceil(items ÷ parallel)`

600 ÷ 2 = **300 rounds**. 601 ÷ 2 = 300.5 → **301 rounds**.

**Step 2. Seconds.** Each round takes about as long as one answer:

`seconds = rounds × seconds per item`

300 × 4 = **1,200 seconds**.

**Step 3. Minutes.** 60 seconds per minute:

`minutes = seconds ÷ 60`

1,200 ÷ 60 = **20 minutes**. Fine at night, too slow for a chat.

How many requests your GPU really handles at once depends on the runner (Ollama's `OLLAMA_NUM_PARALLEL`, LM Studio's settings) and on VRAM. LLMs 2 covers that.

## 🎯 Your quest

1. `batches(items, size)`: split the list into lists of at most `size` items, in order.
2. `run_minutes(n_items, seconds_per_item, parallel)`: steps 1 to 3. Return a float, don't round the minutes.

<details><summary>💡 Hint 1</summary><code>return [items[i:i + size] for i in range(0, len(items), size)]</code></details>
<details><summary>💡 Hint 2</summary><code>return math.ceil(n_items / parallel) * seconds_per_item / 60</code></details>

**Remember:** rounds (round up) × seconds ÷ 60.

## Review

<details><summary>Lesson 9: does the error workflow fire when you click Execute yourself?</summary>No, only for automatic runs.</details>
