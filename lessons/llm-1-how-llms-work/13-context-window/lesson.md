---
title: The context window
xp: 35
---
# Everything the model can see

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

## Your quest

Write `rolling_window(messages, max_tokens)`. Each message is a tuple `(role, token_count)`. The first message is always the system prompt.

- Always keep the system prompt.
- Drop the **oldest** other messages, one at a time, until the total token count is at most `max_tokens`.
- Return the list of kept messages, in their original order.

`total(msgs)` is given. `rest.pop(0)` removes the first item of a list.

## Review

<details><summary>Why divide attention scores by √d?</summary>Dot products grow with the vector length d. Without scaling, softmax becomes almost one-hot and training gradients vanish.</details>
<details><summary>What are query, key and value?</summary>Three vectors computed from each token: the query asks "what am I looking for", the key says "what I contain", the value is what gets passed on when attended to.</details>
<details><summary>Where do most of a transformer's parameters live?</summary>In the MLP (feed-forward) layers.</details>
