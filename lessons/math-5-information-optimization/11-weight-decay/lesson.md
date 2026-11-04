---
title: Regularization and weight decay
xp: 50
---
# Gently shrinking every weight

> **Warm-up:** two models fit the training data equally well. One uses small, calm weights; the other uses huge ones that cancel each other out. Which one would you trust on new data?

**In one sentence:** regularization adds a small penalty for large weights, and weight decay implements it by shrinking every weight by a tiny fraction each step.

## 🪜 Plain words

Big weights often mean the model memorised quirks of the training data (overfitting, LLMs 7). Preferring **small** weights pushes it towards simpler explanations that generalise better.

Two ways to say the same idea:

- **L2 penalty:** add λ/2 · (sum of squared weights) to the loss. Its gradient is λ · w (power rule, Math 3).
- **Weight decay:** each step, multiply every weight by (1 − η · λ), slightly less than 1.

In plain SGD they're identical. In Adam they're not, so **AdamW** applies the decay **separately** ("decoupled"), which works better: that's the "W".

## 🪜 With numbers

η = 0.001, λ = 0.1 → each step multiplies weights by 1 − 0.0001 = **0.9999**.

After 10,000 steps with no gradient pushing back: 0.9999¹⁰⁰⁰⁰ ≈ **0.368** (that's e⁻¹, Math 1 lesson 15). Weights that the data doesn't need fade away; useful ones are held up by their gradients.

Penalty for weights (3, −4) with λ = 0.1: 0.05 · (9 + 16) = **1.25**; gradient (0.3, −0.4).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `λ` | "lambda" | regularization strength (in AdamW: `weight_decay`) | `lam` |
| `‖w‖²` | "norm of w, squared" | sum of squared weights (Math 2) | `sum(x * x for x in w)` |
| `λ/2 ‖w‖²` | "lambda over two times norm w squared" | the L2 penalty (the ½ makes its gradient neat) | |
| `∇` | "grad" | gradient (Math 3) | |
| `(1 − ηλ)` | "one minus eta lambda" | the shrink factor | `1 - lr * lam` |

## 🔬 Take the formulas apart

<div class="formula"><span class="k1">L_total</span> = <span class="k2">L_data</span> + <span class="k3">λ/2</span> · <span class="k4">‖w‖²</span> &nbsp;&nbsp;&nbsp; ∇ of the penalty = <span class="k3">λ</span> · <span class="k5">w</span></div>

<div class="formula"><span class="k5">w</span> ← <span class="k5">w</span> · <span class="k6">(1 − η λ)</span> &nbsp;(then the normal Adam/SGD step)</div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k2">L_data</span> | "L data" | the usual loss | |
| <span class="k4">‖w‖²</span> | "norm w squared" | how big the weights are | 9 + 16 = 25 |
| <span class="k3">λ/2</span> | "lambda over two" | how much we care | 0.05 |
| <span class="k6">(1 − ηλ)</span> | "one minus eta lambda" | per-step shrink | 0.9999 |

## 🔀 What if it were different?

<div class="wrong"><b>Multiply by (1 − λ) instead of (1 − ηλ)</b>: × 0.9 every step → after 50 steps weights are at 0.5% of their size. The model is wiped out.</div>
<div class="wrong"><b>w · (1 + ηλ)</b>: weights grow every step; the opposite of regularization, eventually inf.</div>
<div class="wrong"><b>λ = 0 on a tiny dataset</b>: nothing stops memorisation; validation loss rises while training loss falls (LLMs 7's overfitting diagnosis).</div>
<div class="right">shrink by 0.9999 per step → 0.368 after 10,000 steps ✓</div>

## 🗣️ Say it out loud

"w becomes w times one minus eta lambda."

## 🤖 Where AI uses it

`AdamW(lr=3e-4, weight_decay=0.1)` is the default LLM recipe. Biases and LayerNorm weights are usually excluded from decay. Dropout and early stopping are other regularizers (LLMs 6).

## 🎯 Your quest

1. `l2_penalty(ws, lam)`: λ/2 · Σ w².
2. `l2_grad(ws, lam)`: list of λ · w.
3. `decay(ws, lr, lam)`: list of w · (1 − lr · lam).

**Remember:** regularization = prefer small weights; weight decay shrinks a tiny bit every step.

## Review

<details><summary>Why does Adam divide by √v̂?</summary>So each weight's step is about lr, whatever its gradient scale.</details>
<details><summary>What is ε for?</summary>To never divide by 0.</details>
