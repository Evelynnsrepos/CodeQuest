---
title: Batches for one GPU
minutes: 35
xp: 30
hint: batches: groups = [] and current = [], then for item in items: and inside it current.append(item)
hint: Still in the loop: if len(current) == size: then groups.append(current) and current = []
hint: After the loop: if len(current) > 0: groups.append(current). Then return groups
hint: run_minutes is one line: return math.ceil(n_items / parallel) * seconds_per_item / 60
---
# Don't send 500 items to one graphics card at once

⏱️ About 35 minutes · two small functions

> **Warm-up:** 600 emails go into an Ollama node. Your GPU can answer about 2 at once, 4 seconds each. Roughly how long will it take, and what happens if n8n fires all 600 at once?

**In one sentence:** with a local model your GPU is the bottleneck, so feed it items in **batches** (the *Loop Over Items* node), turn on **Retry On Fail**, and estimate the run time before you start.

## 🪜 The n8n settings

- **Loop Over Items** (also called Split in Batches): passes items on in groups of a size you choose, and loops until all are done.
- Each node's **Settings** tab: **Retry On Fail**, **Max Tries**, **Wait Between Tries (ms)**. Good for a model that's still loading.
- **Timeout** in the workflow settings, so a stuck run ends.

## 🪜 Run-time math, one step at a time

**Step 1. Rounds.** If the GPU handles `parallel` requests at once, the items go through in rounds. The number of rounds is items ÷ parallel, rounded **up** (the last round may be half full):

`rounds = ceil(items ÷ parallel)`

`ceil` (say "ceiling") means "round up to the next whole number": ceil(300.5) = 301, ceil(300) = 300.

600 ÷ 2 = **300 rounds**. 601 ÷ 2 = 300.5 → **301 rounds**.

**Step 2. Seconds.** Each round takes about as long as one answer:

`seconds = rounds × seconds per item`

300 × 4 = **1,200 seconds**.

**Step 3. Minutes.** 60 seconds per minute:

`minutes = seconds ÷ 60`

1,200 ÷ 60 = **20 minutes**. Fine at night, too slow for a chat.

How many requests your GPU really handles at once depends on the runner (Ollama's `OLLAMA_NUM_PARALLEL`, LM Studio's settings) and on VRAM. LLMs 2 covers that.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `current = []` | | the batch you're filling right now |
| `len(current) == size` | "the length of current equals size" | true when the batch is full |
| `groups.append(current)` | | puts the full batch into the list of batches. A list **inside** a list is fine. |
| `current = []` | | starts a new, empty batch. The old one is safe inside `groups`. |
| `len(current) > 0` | "current isn't empty" | after the loop: is there a half-full last batch left? |
| `math.ceil(x)` | "ceiling of x" | rounds up: `math.ceil(300.5)` is `301` |

### 👀 Worked example: eggs into boxes of 4

```python
def egg_boxes(eggs, size):
    boxes = []
    box = []
    for egg in eggs:
        box.append(egg)
        if len(box) == size:
            boxes.append(box)
            box = []
    if len(box) > 0:
        boxes.append(box)
    return boxes

print(egg_boxes(["e1", "e2", "e3", "e4", "e5"], 4))
```

1. e1, e2, e3 go into `box`. Its length is 1, 2, 3: not full yet.
2. e4: length 4 = full. The box goes into `boxes`, and `box` starts empty again.
3. e5 goes into the new box. Length 1.
4. The loop is over, but `box` still holds e5. `len(box) > 0`, so it's added too.
5. Returns `[["e1", "e2", "e3", "e4"], ["e5"]]`.

Without step 4, the last egg would be lost.

## 🎯 Your quest

**Part 1:** `batches(items, size)`. Replace `return [items]` with:

1. `groups = []`
2. `current = []`
3. `for item in items:`
4. `    current.append(item)`
5. `    if len(current) == size:`
6. `        groups.append(current)`
7. `        current = []`
8. `if len(current) > 0:`
9. `    groups.append(current)`
10. `return groups`

**Part 2:** `run_minutes(n_items, seconds_per_item, parallel)`: steps 1 to 3 in one line. Don't round the minutes. Replace `return 0` with:

1. `return math.ceil(n_items / parallel) * seconds_per_item / 60`

Read it from the left: rounds (rounded up), times the seconds per item, divided by 60.

**Remember:** rounds (round up) × seconds ÷ 60.

## Review

<details><summary>Lesson 9: does the error workflow fire when you click Execute yourself?</summary>No, only for automatic runs.</details>
