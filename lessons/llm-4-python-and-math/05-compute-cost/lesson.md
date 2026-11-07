---
title: Counting the cost in FLOPs
minutes: 40
xp: 35
hint: matmul_flops: return 2 * m * k * n
hint: training_flops: return 6 * params * tokens
hint: training_days: seconds = flops / (tflops * 1e12 * utilization), then return seconds / 86400
hint: 1e12 is Python for 10¹², a 1 with 12 zeros
---
# How much compute does a model need?

⏱️ About 40 minutes

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

## 🔬 Take the formulas apart

**Big numbers.** `10¹²` ("ten to the twelve") is a 1 with 12 zeros: 1,000,000,000,000 (a trillion). The small raised number says how many times you multiply by 10. Python writes it `1e12`: "1 times ten to the 12". So `8e9` is 8 × 10⁹ = 8,000,000,000 (8 billion) and `15e12` is 15 trillion.

**Multiplying powers of ten:** add the small numbers. 10⁹ × 10¹² = 10²¹. That's why the Llama number gets so big so fast.

**A matmul's cost** <div class="formula">FLOPs ≈ <span class="k1">2</span> · <span class="k2">m · n</span> · <span class="k3">k</span></div>
- `≈` means "about equal to".
- <span class="k2">m · n</span>: the result has m × n entries.
- <span class="k3">k</span>: each entry is a dot product of length k, so k multiplications…
- <span class="k1">2</span>: …and about k additions. Multiply + add = 2 operations per pair.

Numbers: (2 × 3) @ (3 × 4): 2 × 2 × 3 × 4 = **48** FLOPs.

**Training cost** <div class="formula">training ≈ <span class="k1">6</span> · <span class="k2">N</span> · <span class="k3">T</span></div>
<span class="k2">N</span> = parameters (weights), <span class="k3">T</span> = training tokens. For every token, every weight is used in the forward pass (2 FLOPs) and the backward pass (about 4 more): <span class="k1">6</span> in total.

Numbers: a 1-billion-parameter model on 20 billion tokens: 6 × 10⁹ × 20 × 10⁹ = 120 × 10¹⁸ = **1.2 × 10²⁰** FLOPs.

**Time** <div class="formula">seconds = <span class="k1">FLOPs</span> / (<span class="k2">TFLOPS × 10¹²</span> × <span class="k3">utilization</span>)</div>
- <span class="k2">TFLOPS × 10¹²</span>: how many FLOPs the GPU can do per second at full speed ("tera" = 10¹²).
- <span class="k3">utilization</span>: the share it really reaches, like 0.4 for 40%.
- Divide the work by the speed to get seconds, then divide by 86,400 (= 24 hours × 60 minutes × 60 seconds) to get days.

Numbers: 86,400 × 10¹² FLOPs on a 2-TFLOPS GPU at 50%: speed = 2 × 10¹² × 0.5 = 10¹² per second, time = 86,400 seconds = **1 day**.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `2 * m * k * n` | | multiply all of them. `*` is "times". |
| `1e12` | "one e twelve" | 10¹², a trillion |
| `a / b` | "a divided by b" | division. The answer can have decimals. |
| `seconds = …` then `return seconds / 86400` | | store a step in a name first, then use it. Easier to read. |

### 👀 Worked example: how long to read a library?

```python
def reading_days(pages, pages_per_minute, awake_share):
    minutes = pages / (pages_per_minute * awake_share)
    return minutes / 1440
```

10,000 pages, 2 pages per minute, awake and reading half of the time (0.5): minutes = 10,000 / (2 × 0.5) = 10,000. A day has 1,440 minutes, so about **6.9 days**. Same shape as `training_days`: work ÷ (speed × share), then convert the unit.

## 🎯 Your quest

Replace each `return 0` (4 spaces inside each function):

`matmul_flops(m, k, n)`: `    return 2 * m * k * n`

`training_flops(params, tokens)`: `    return 6 * params * tokens`

`training_days(flops, tflops, utilization)`:

1. `    seconds = flops / (tflops * 1e12 * utilization)`
2. `    return seconds / 86400`

Run it. Llama 3 8B would take about **2,200 years** on one consumer GPU; your toy model about **10 minutes**.

## Review

<details><summary>What is the shape rule for matrix multiplication?</summary>(m × k) @ (k × n) gives m × n; the inner sizes must match.</details>
<details><summary>Why are batches of tokens processed as one matmul?</summary>Stacking token vectors as rows turns many matrix-vector products into one matrix-matrix product, which GPUs do very efficiently.</details>
<details><summary>What is 10³ × 10⁴?</summary>10⁷: add the small numbers, 3 + 4 = 7.</details>
