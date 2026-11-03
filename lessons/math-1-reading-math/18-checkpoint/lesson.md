---
title: Checkpoint: read a real AI formula
xp: 60
---
# Softmax, straight from the paper

> **Warm-up:** here's a formula from real AI papers: `softmax(z)ᵢ = e^(zᵢ) / Σⱼ e^(zⱼ)`. Don't panic. Just find the signs you recognise.

## 🪜 Plain words

A model gives every possible next word a **score**. Scores can be anything: 2, −1, 0.1. We want **chances** instead: all positive, adding up to 100%. Two steps:

1. Make every score positive (with e, which is always positive, and keeps bigger scores bigger).
2. Divide each by the total, so they add up to 1.

## 🪜 With numbers

Scores 2, 1, 0.1:

1. e² ≈ 7.39, e¹ ≈ 2.72, e^0.1 ≈ 1.11. All positive.
2. Total: 7.39 + 2.72 + 1.11 = 11.22.
3. Divide: 7.39/11.22 ≈ **0.66**, 2.72/11.22 ≈ **0.24**, 1.11/11.22 ≈ **0.10**. They add up to 1 ✓.

## 🔬 Take the formula apart

<div class="formula"><span class="k1">softmax(z)</span><sub><span class="k2">i</span></sub> = <span class="k3">e</span><sup><span class="k4">zᵢ</span></sup> / <span class="k5">Σ</span><sub><span class="k6">j</span></sub> <span class="k3">e</span><sup><span class="k4">zⱼ</span></sup></div>

| Piece | Say it | Means | For the first score |
|---|---|---|---|
| <span class="k1">softmax(z)</span> | "softmax of z" | a function (machine) that takes the whole list of scores z | z = (2, 1, 0.1) |
| <sub><span class="k2">i</span></sub> | "sub i" / "item i" | we're computing the output for position i | i = 1 |
| <span class="k3">e</span><sup><span class="k4">zᵢ</span></sup> | "e to the z i" | e raised to score number i: always positive | e² ≈ 7.39 |
| `/` (fraction bar) | "divided by" | top divided by the whole bottom (invisible brackets!) | |
| <span class="k5">Σ</span> | "the sum of" | add up… | |
| <sub><span class="k6">j</span></sub> | "over j" | …for every position j. A **new** letter, because i is already busy meaning "the one we're computing" | j = 1, 2, 3 |
| <span class="k3">e</span><sup><span class="k4">zⱼ</span></sup> | "e to the z j" | e raised to each score | 7.39 + 2.72 + 1.11 = 11.22 |
| result | | | 7.39 / 11.22 ≈ 0.66 |

And the **loss** for the correct token t:

<div class="formula"><span class="k1">L</span> = <span class="k2">−</span><span class="k3">log</span> <span class="k4">softmax(z)ₜ</span></div>

| Piece | Say it | Means | If t is the first token |
|---|---|---|---|
| <span class="k1">L</span> | "L" | the loss: how wrong the model was | 0.42 |
| <span class="k4">softmax(z)ₜ</span> | "softmax of z, item t" | the chance the model gave the **right** token | 0.66 |
| <span class="k3">log</span> | "log" | natural log: of a number below 1 it's negative | ln 0.66 ≈ −0.42 |
| <span class="k2">−</span> | "minus" | flip the sign so the loss is positive | 0.42 |

Right token got 0.99 → L ≈ 0.01 (almost perfect). Got 0.01 → L ≈ 4.6 (very wrong).

## 🔀 What if the formula were different?

<div class="wrong"><b>zᵢ / Σⱼ zⱼ</b> (no e): scores (2, −1, 0.1) sum to 1.1, so the "chance" of the second is −1/1.1 = −0.91. Negative probability: impossible.</div>
<div class="wrong"><b>e^(zᵢ) / Σⱼ zⱼ</b> (e only on top): 7.39 / 3.1 ≈ 2.4, a "probability" of 240%.</div>
<div class="wrong"><b>Using i inside the sum too (Σᵢ e^(zᵢ))</b>: confusing, because i would mean two things at once. That's why papers switch to j.</div>
<div class="wrong"><b>L = log softmax(z)ₜ</b> (no minus): the loss is negative and gets <i>more</i> negative as the model gets better. Minimizing it would make the model worse.</div>
<div class="right">e on top and bottom, a fresh letter j for the sum, minus in front of the log ✓</div>

## 🗣️ Say it out loud

"Item i of softmax of z equals e to the z i, divided by the sum over all j of e to the z j." And: "The loss is minus the log of the probability of the right token."

## 🎯 Your quest

1. `softmax(z)`: return the list of `e^(zᵢ) / Σⱼ e^(zⱼ)`.
2. `cross_entropy(z, t)`: `−log softmax(z)ₜ` with the natural log.

You just read the formula at the heart of every LLM. Next: Math 2, vectors and matrices.

## Review

<details><summary>What does θ usually mean?</summary>All the model's weights.</details>
<details><summary>What does ← mean?</summary>"Becomes": an update.</details>
<details><summary>What is log(1)?</summary>0.</details>
