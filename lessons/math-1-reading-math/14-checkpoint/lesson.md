---
title: Checkpoint: read a real formula
xp: 60
---
# Softmax, straight from the paper

> **Warm-up:** cover the explanation below and try to say this out loud: `softmax(z)ᵢ = e^(zᵢ) / Σⱼ e^(zⱼ)`.

Everything in this course is in that one formula. Piece by piece:

| Piece | Say it | Meaning |
|---|---|---|
| `z` | "z" | a list of scores (logits), `z ∈ ℝⁿ` |
| `softmax(z)ᵢ` | "softmax of z, item i" | the i-th output; a function (lesson 7) applied to a list, then indexed (lesson 8) |
| `e^(zᵢ)` | "e to the z i" | exp of score i: always positive (lesson 11) |
| `Σⱼ e^(zⱼ)` | "the sum over j of e to the z j" | add up exp of **every** score. A new letter `j` because `i` is already taken (lesson 8) |
| the fraction | "over" | the whole top divided by the whole bottom (lesson 2) |

🗣️ "Item i of softmax is e to the z i, divided by the sum of e to the z j over all j." → "Make every score positive with exp, then divide by the total, so they add up to 1." The result is a probability distribution (lesson 12).

The second formula, **cross-entropy loss** for the correct token `t`:

```
L = −log softmax(z)ₜ
```

🗣️ "L equals minus the log of the softmax probability of the correct token." → small when the model gave the right token a high probability (log of nearly 1 is nearly 0), huge when it gave it a tiny one (lesson 10).

## 🎯 Your quest

Write both straight from the notation:

1. `softmax(z)`: return the list of `e^(zᵢ) / Σⱼ e^(zⱼ)`.
2. `cross_entropy(z, t)`: `−log softmax(z)ₜ`, with the natural log.

You've now read the formula at the heart of every LLM. Math 2 (vectors and matrices) is next.

## Review

<details><summary>What does θ usually mean?</summary>All the model's parameters (weights).</details>
<details><summary>What does ← mean in θ ← θ − η∇L?</summary>"Is replaced by": an update, like assignment.</details>
<details><summary>What is log(1)?</summary>0.</details>
