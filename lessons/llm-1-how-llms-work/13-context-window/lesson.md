---
title: The context window
minutes: 30
xp: 35
hint: Replace the comment with a while loop: while len(rest) > 0 and total([system] + rest) > max_tokens:
hint: Inside the while loop (8 spaces): rest.pop(0)
---
# Everything the model can see

⏱️ About 30 minutes

> **Warm-up:** where does the model keep the memory of your conversation between two messages?

Nowhere. The weights never change while you chat, and the model has no memory of its own. Every time you send a message, LM Studio sends the **whole conversation again** (as one templated string) and the model reads it from scratch. The **context window** is the maximum number of tokens it can take in at once, and *everything* shares it:

```
┌──────────── context window (e.g. 8,192 tokens) ────────────┐
│ system prompt │ earlier messages │ tool results │ your msg │ ← reply │
└────────────────────────────────────────────────────────────┘
```

The reply is generated *inside* the same window, so it needs room too.

**Why is there a limit?**

- **Training length.** The model learns word positions through a position encoding (most modern models use **RoPE**, rotary position embeddings). It works reliably for the lengths it was trained on; far beyond that, quality collapses. The model card lists the supported length.
- **Compute.** In attention every token scores every earlier token, so the work grows with the *square* of the length: 2× the context is ~4× the attention work.
- **Memory.** The KV cache grows with every token. In LM Studio you choose the **Context Length** when you load a model, and a bigger setting reserves more VRAM even if you never use it (Module 2 computes how much).

**Causal masking.** During generation a token can only attend to tokens *before* it, never after. During training, a mask hides the future so the model can't cheat by peeking at the token it's supposed to predict.

**When the chat gets too long**, something has to give. Apps either refuse, or drop text: the common strategy is a **rolling window** that keeps the system prompt and throws away the *oldest* messages. LM Studio has a setting for this (called "Context Overflow" in recent versions, with options like rolling window, truncate middle and stop at limit; check your version). The dropped messages are simply *not in the input anymore*, so the model cannot know they existed.

Even inside the window, models use long contexts unevenly: facts in the middle of a very long prompt are recalled worse than those at the start or end ("lost in the middle", Liu et al., 2023).

## 🐍 Python you need

The starter already splits the chat: `system` is the first message, `rest` is a list of all the others. Each message is a pair like `("user", 1200)`: who, and how many tokens.

| You write | Say it | What it does |
|---|---|---|
| `total(msgs)` | | given: adds up the token counts of a list of messages |
| `[system] + rest` | "system, plus the rest" | puts the system prompt back in front: a new list with everything still kept |
| `while condition:` | "while … is true" | repeats the lines under it **as long as** the condition is true. It checks again before every round. |
| `len(rest) > 0` | "rest isn't empty" | there's still something left to drop |
| `a and b` | | true only when both are true |
| `rest.pop(0)` | "rest pop zero" | removes the **first** (oldest) item from the list |

### 👀 Worked example: a full suitcase

Take out the oldest-packed item until the suitcase weighs at most 10 kg:

```python
items = [4, 3, 5, 2]
while len(items) > 0 and sum(items) > 10:
    items.pop(0)
print(items)   # [3, 5, 2]
```

| round | before | sum | > 10? | after |
|---|---|---|---|---|
| 1 | [4, 3, 5, 2] | 14 | yes | pop 4 → [3, 5, 2] |
| 2 | [3, 5, 2] | 10 | **no** | the loop stops |

10 is not **more** than 10, so it stops at `[3, 5, 2]`: "at most 10" includes 10 itself.

The `len(items) > 0` part makes sure the loop stops even if nothing is left to remove.

## 🎯 Your quest

Write `rolling_window(messages, max_tokens)`: always keep the system prompt, drop the **oldest** other messages one at a time until everything fits. Replace the comment line with:

1. `while len(rest) > 0 and total([system] + rest) > max_tokens:`
2. `    rest.pop(0)`

The `return [system] + rest` line is already there.

## Review

<details><summary>Why divide attention scores by √d?</summary>Dot products grow with the vector length d. Without scaling, softmax becomes almost one-hot and training gradients vanish.</details>
<details><summary>What are query, key and value?</summary>Three vectors computed from each token: the query asks "what am I looking for", the key says "what I contain", the value is what gets passed on when attended to.</details>
<details><summary>Where do most of a transformer's parameters live?</summary>In the MLP (feed-forward) layers.</details>
<details><summary>What is the difference between while and for?</summary>for goes through a list once per item. while repeats as long as a condition is true, checking it again every round.</details>
