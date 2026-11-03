---
title: Multi-head attention
xp: 50
---
# Many heads look at different things

> **Warm-up:** one attention head produces one set of weights per token. Can a single set of weights track both "which noun does *it* refer to" and "which word came right before me"?

Not well. So a transformer layer runs **several heads in parallel**. With model width `d = 4096` and `h = 32` heads (Llama 3 8B), each head works on `d / h = 128` numbers:

1. Compute Q, K, V for every position as usual (each a `d`-wide row).
2. **Split** each row into `h` slices of `d/h` numbers. Slice number `i` of every row belongs to head `i`.
3. Run causal attention **per head** on its slices.
4. **Concatenate** the heads' outputs back into one `d`-wide row per position, then multiply by an output matrix `W_O` (skipped here).

It costs the same as one big head (the slices add up to `d`), but each head gets its own softmax, so each can attend somewhere different. Interpretability research found heads that do specific jobs, such as **induction heads**, which copy patterns ("A B … A → B") and are a big part of in-context learning.

**Causal** means position `i` only attends to positions `0..i`: a model that predicts the next token must not peek at it. In real code this is a **mask** that sets future scores to −∞ before the softmax.

Modern variant: **grouped-query attention (GQA)** lets several query heads share one K/V head (Llama 3 8B: 32 query heads, 8 K/V heads), which shrinks the KV cache 4×. You met its effect in LLMs 2's VRAM math.

## Python you need

Slicing: `row[2:4]` is items 2 and 3. Joining lists: `a + b`, or `sum(lists, [])` for many.

## Your quest

`causal_attention` (one head) is given.

1. `split_heads(rows, n_heads)`: return a list with one entry per head; entry `h` is the list of every row's slice `h` (slice width `len(row) // n_heads`).
2. `multi_head(Q, K, V, n_heads)`: split Q, K and V, run `causal_attention` per head, then for each position join the heads' output rows in head order.

## Review

<details><summary>Why divide attention scores by √d?</summary>Dot products grow with vector length; without scaling the softmax saturates and gradients vanish.</details>
<details><summary>What is a harness?</summary>The program around a model that builds prompts, runs tools, loops, manages context and asks for permissions.</details>
