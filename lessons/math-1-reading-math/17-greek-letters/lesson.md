---
title: The Greek letters of AI
xp: 30
---
# A cheat sheet for the alphabet papers use

> **Warm-up:** how many Greek letters have you met so far? (Hint: π, Σ, Π, σ…)

**In one sentence:** math uses Greek letters as extra variable names, and in AI most of them have a usual meaning you can learn once.

## 🪜 Plain words

Math ran out of normal letters, so it borrowed the Greek alphabet. A Greek letter is **just a name for a number** (or a list of numbers), exactly like `x`. The only thing to learn is what each one usually stands for. Papers always say it somewhere, often right after the formula: "where θ denotes the model parameters".

## 🔣 The letters you'll meet most

| Letter | Say it | Usual meaning in AI |
|---|---|---|
| `α` | "alpha" | learning rate, or a mixing weight (LoRA's α) |
| `β` | "beta" | Adam's β₁, β₂; strength of a KL penalty |
| `γ` | "gamma" | discount in RL; LayerNorm's gain |
| `δ` | "delta" | a small change, an error signal |
| `Δ` | "delta" (capital) | "change in": Δx = new x − old x |
| `ε` | "epsilon" | a tiny number to avoid dividing by 0 (`1e-8`), or noise |
| `η` | "eta" | learning rate (some papers) |
| `θ` | "theta" | **all the model's weights** |
| `λ` | "lambda" | strength of regularization (weight decay); eigenvalue |
| `μ` | "mu" (mew) | mean (average) |
| `π` | "pie" | 3.14159…, or a **policy** in RL: `π(a \| s)` |
| `ρ` | "rho" (row) | a ratio (PPO) |
| `σ` | "sigma" | standard deviation, or the sigmoid |
| `Σ` | "sigma" (capital) | sum |
| `τ` | "tau" (tow) | temperature |
| `∇` | "nabla" / "grad" | the gradient (Math 3) |
| `∂` | "partial" / "del" | partial derivative (Math 3) |

## 🔬 Take the formula apart

The training update (you'll fully understand it in Math 3):

<div class="formula"><span class="k1">θ</span> <span class="k2">←</span> <span class="k1">θ</span> <span class="k3">−</span> <span class="k4">η</span> <span class="k5">∇L(θ)</span></div>

| Piece | Say it | Means |
|---|---|---|
| <span class="k1">θ</span> (left) | "theta" | the new weights |
| <span class="k2">←</span> | "becomes" / "is replaced by" | an **update**, like Python's `=` (not "equals") |
| <span class="k1">θ</span> (right) | "theta" | the old weights |
| <span class="k3">−</span> | "minus" | step **away** from… |
| <span class="k4">η</span> | "eta" | the learning rate: how big a step (like 0.001) |
| <span class="k5">∇L(θ)</span> | "the gradient of L at theta" | the direction in which the loss L grows fastest |

## 🔀 What if the formula were different?

<div class="wrong"><b>θ ← θ + η∇L</b> (plus instead of minus): you'd step <i>uphill</i>, making the loss bigger every step. Training gets worse and worse.</div>
<div class="wrong"><b>θ ← η∇L</b> (forgot the old θ): every step throws away everything learned so far.</div>
<div class="wrong"><b>η = 1000</b> instead of 0.001: steps so huge they jump right over the valley; the loss explodes.</div>
<div class="right"><b>θ ← θ − η∇L(θ)</b>: a small step downhill ✓</div>

## 🗣️ Say it out loud

"Theta becomes theta minus eta times the gradient of L at theta."

## 🎯 Your quest

Fill `MEANING` with the usual AI meaning (lowercase, exactly one of: `"learning rate"`, `"parameters"`, `"standard deviation"`, `"mean"`, `"tiny number"`, `"change"`).

**Remember:** θ = the weights. When unsure, look for "where … denotes".

## Review

<details><summary>Python for "x ∈ [0, 1)"?</summary>0 <= x < 1</details>
<details><summary>What does ∀ mean?</summary>"For all".</details>
