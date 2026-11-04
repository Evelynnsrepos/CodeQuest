---
title: Checkpoint: read a model's report card
xp: 90
---
# Loss, perplexity and uncertainty from raw logits

> **Warm-up:** a model outputs logits for 3 tokens of text. What would you compute to say how good and how sure it is?

You'll turn raw logits into the three numbers every LLM report shows, using only what this course taught, in a numerically safe way.

## 🪜 The plan

For each position you get a logit list and the index of the true next token.

1. **log-softmax** with log-sum-exp (lesson 06), never overflowing.
2. **loss** = average of −log p(correct) (lesson 03), in nats.
3. **perplexity** = e^loss (lesson 05).
4. **entropy** of each position's distribution (lesson 02, in nats), averaged: how unsure the model is, whether or not it's right.

## 🔬 The formulas, one more time

<div class="formula"><span class="k1">log pᵢ</span> = <span class="k2">zᵢ</span> − <span class="k3">LSE(z)</span> &nbsp; <span class="k4">loss</span> = − <span class="k5">1/N Σₜ</span> <span class="k1">log p<sub>yₜ</sub></span> &nbsp; <span class="k6">PPL</span> = e<sup><span class="k4">loss</span></sup></div>

| Piece | Means |
|---|---|
| <span class="k2">zᵢ</span> − <span class="k3">LSE(z)</span> | safe log-probability of token i |
| <span class="k1">log p<sub>yₜ</sub></span> | log-probability of the true token at position t |
| <span class="k5">1/N Σₜ</span> | average over positions |
| <span class="k4">loss</span> | cross-entropy in nats |
| <span class="k6">PPL</span> | effective number of choices |

## 🔀 What if it were different?

<div class="wrong"><b>Plain softmax then log</b>: logits like (0, −1000) give p = 0.0 → log(0) error. LSE gives −1000.</div>
<div class="wrong"><b>Confusing entropy with loss</b>: a model can be very sure (low entropy) and very wrong (high loss). That combination is the dangerous one: confident hallucination.</div>
<div class="right">all three from log-softmax, averaged per position ✓</div>

## 🎯 Your quest

`evaluate(logits_list, targets)`: return a dict with `"loss"`, `"ppl"` and `"entropy"` (all in nats). If the loss is too big for `math.exp` (above about 709), report the perplexity as `math.inf`.

You've finished the Math for AI track. Every formula in the LLM courses is now yours to read.

## Review

<details><summary>Adam's step in words?</summary>Bias-corrected average direction ÷ typical size, times lr.</details>
<details><summary>Why multiply distillation loss by T²?</summary>Softening by T shrinks gradients by about T²; this undoes it.</details>
<details><summary>Biggest safe learning rate for curvature c?</summary>2 / c.</details>
