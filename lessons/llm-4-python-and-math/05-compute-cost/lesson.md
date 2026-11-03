---
title: Counting the cost in FLOPs
xp: 35
---
# How much compute does a model need?

> **Warm-up:** Llama 3 8B was trained on about 15 trillion tokens. Could your GPU do that in a year? Guess before calculating.

Compute is measured in **FLOPs**: floating-point operations (one multiply or one add). A matrix multiplication `(m × k) @ (k × n)` makes `m·n` outputs, each a dot product of length `k` (k multiplies, k adds), so:

```
matmul FLOPs ≈ 2 · m · k · n
```

Since almost all of an LLM's work is matmuls with its weights, two famous rules of thumb follow (`N` = parameters, `T` = tokens):

```
inference ≈ 2 · N FLOPs per token          (each weight: one multiply, one add)
training  ≈ 6 · N · T FLOPs in total       (forward 2N + backward ≈ 4N, per token)
```

(Attention over long contexts adds more, but for typical lengths these are close.)

How many tokens should you train on? The **Chinchilla** paper (Hoffmann et al., 2022) found that for the best model *for a fixed compute budget*, use about **20 tokens per parameter**. Modern small models go far beyond that (Llama 3 8B: ~1,900 tokens per parameter), because a smaller model trained longer is cheaper to *run* for millions of users.

GPUs are rated in **TFLOPS** (10¹² FLOPs per second) for 16-bit math. Real training reaches perhaps 30–50% of that (**utilization**, MFU). Look up your card's FP16 TFLOPS; for example, an RX 6700 XT is rated around 26.

## Your quest

1. `matmul_flops(m, k, n)`
2. `training_flops(params, tokens)`
3. `training_days(flops, tflops, utilization)`: `flops ÷ (tflops × 10¹² × utilization)` seconds, converted to days (86,400 seconds per day).

Then run it: how long would Llama 3 8B take on one consumer GPU, and how long would a 10M-parameter toy model take on 100M tokens (the kind you'll train in Module 5)?

## Review

<details><summary>What is the shape rule for matrix multiplication?</summary>(m × k) @ (k × n) gives m × n; the inner sizes must match.</details>
<details><summary>Why are batches of tokens processed as one matmul?</summary>Stacking token vectors as rows turns many matrix-vector products into one matrix-matrix product, which GPUs do very efficiently.</details>
