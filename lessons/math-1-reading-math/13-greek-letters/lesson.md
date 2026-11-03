---
title: The Greek letters of AI
xp: 30
---
# A cheat sheet for the alphabet papers use

> **Warm-up:** how many Greek letters do you already recognise? (You've met π, Σ and σ.)

**In one sentence:** math uses Greek letters as extra variable names, and in AI most of them have a usual meaning you can learn once.

## 🔣 The letters you'll meet most

| Letter | Name (say it) | Usual meaning in AI |
|---|---|---|
| `α` | alpha | learning rate, or a mixing weight (LoRA's α) |
| `β` | beta | Adam's decay rates β₁, β₂; the KL penalty strength |
| `γ` | gamma | discount factor in RL; LayerNorm's gain |
| `δ` | delta | a small change, an error signal |
| `Δ` | Delta (capital) | "change in": `Δx = x_new − x_old` |
| `ε` | epsilon | a tiny number to avoid dividing by 0 (`1e-8`), or noise in diffusion |
| `η` | eta | learning rate (some papers) |
| `θ` | theta | **all the model's parameters** (weights) |
| `λ` | lambda | regularization strength (weight decay) |
| `μ` | mu | mean of a distribution |
| `π` | pi | 3.14159…, or a **policy** in RL (`π(a \| s)`) |
| `ρ` | rho | a ratio (PPO), a correlation |
| `σ` | sigma | standard deviation, or the sigmoid function |
| `Σ` | Sigma (capital) | sum; or a covariance matrix |
| `τ` | tau | temperature (sometimes T) |
| `φ`, `ψ` | phi, psi | parameters of a second network |
| `ω` | omega | weights, frequencies |
| `∇` | nabla / "del" (not Greek, but looks it) | gradient (Math 3) |
| `∂` | "partial" / "del" | partial derivative (Math 3) |

Meaning depends on the paper: **always check where a letter is defined**, usually right after the formula ("where θ denotes the model parameters").

## 🗣️ Say it out loud

`θ ← θ − η ∇L(θ)` → "theta becomes theta minus eta times the gradient of L at theta" → "update the weights by taking a small step downhill on the loss" (gradient descent, Math 3).

`←` means "is replaced by": this one *is* an assignment, like Python's `=`.

## 🎯 Your quest

Fill in `MEANING` with the usual AI meaning from the table (lowercase, exactly one of: `"learning rate"`, `"parameters"`, `"standard deviation"`, `"mean"`, `"tiny number"`, `"change"`).

**Remember:** θ = the weights. When in doubt, look for "where … denotes".

## Review

<details><summary>Python for "x ∈ [0, 1)"?</summary>0 <= x < 1</details>
<details><summary>What does ∀ mean?</summary>"For all".</details>
