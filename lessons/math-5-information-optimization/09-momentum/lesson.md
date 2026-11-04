---
title: Moving averages and momentum
xp: 55
---
# A rolling ball doesn't stop at every bump

> **Warm-up:** your training loss jumps around: 2.3, 2.1, 2.4, 2.0, 2.2. How could you draw a smoother line that still follows the trend?

**In one sentence:** an exponential moving average keeps a running blend "mostly the old value, a bit of the new one", and momentum uses that idea so gradient steps keep their direction instead of zig-zagging.

## 🪜 Plain words

**Exponential moving average (EMA):** keep one number s. For each new value x: s = 0.9 · s + 0.1 · x. Old values fade slowly, noise gets smoothed out. The 0.9 is β: bigger β = smoother but slower to react.

**Momentum:** instead of stepping along the raw gradient (noisy, zig-zagging across a narrow valley), keep a **velocity** that accumulates gradients: v = β · v + g. Directions that keep agreeing add up and speed up; directions that flip back and forth cancel out. Like a ball rolling downhill.

## 🪜 With numbers

EMA with β = 0.9, starting at s = 0, values 1, 1, 1: s = **0.1, 0.19, 0.271**… slowly heading to 1. (It starts biased towards 0. Adam fixes this, next lesson.)

Momentum with β = 0.9, same gradient 1 every step: v = **1, 1.9, 2.71, …** → heads to 1 / (1 − 0.9) = **10**. A steady slope gets up to 10× bigger steps.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `β` | "beta" | how much of the old value to keep (0.9 typical) | `beta` |
| `sₜ` | "s t" | the average after step t | `s` |
| `vₜ` | "v t" | velocity after step t | `v` |
| `gₜ` | "g t" | gradient at step t | `g` |
| `sₜ₋₁` | "s t minus one" | the previous value | |
| `1 / (1 − β)` | "one over one minus beta" | the long-run speed-up / the "memory length" | `1 / (1 - beta)` |

## 🔬 Take the formulas apart

<div class="formula"><span class="k1">sₜ</span> = <span class="k2">β</span> · <span class="k3">sₜ₋₁</span> + <span class="k4">(1 − β)</span> · <span class="k5">xₜ</span></div>

| Piece | Say it | Means | β = 0.9, x = 1, s = 0.1 |
|---|---|---|---|
| <span class="k3">sₜ₋₁</span> | "s t minus one" | previous average | 0.1 |
| <span class="k2">β</span> · | "beta times" | keep 90% of it | 0.09 |
| <span class="k4">(1 − β)</span> · <span class="k5">xₜ</span> | "one minus beta, times x t" | blend in 10% of the new value | 0.1 |
| <span class="k1">sₜ</span> | "s t" | new average | 0.19 |

<div class="formula"><span class="k6">v</span> ← <span class="k2">β</span> <span class="k6">v</span> + <span class="k5">g</span> &nbsp;&nbsp;&nbsp; θ ← θ − η <span class="k6">v</span></div>

## 🔀 What if it were different?

<div class="wrong"><b>EMA with β and (1 − β) swapped</b>: s = 0.1 · s + 0.9 · x. Barely smooths anything: almost just the newest value.</div>
<div class="wrong"><b>EMA without (1 − β)</b>: s = 0.9 s + x → heads to 10, not 1. The "average" is 10× too big (that's momentum's form, fine for velocity, wrong for an average).</div>
<div class="wrong"><b>β = 1</b>: v never forgets, keeps growing forever; the ball never stops at the bottom.</div>
<div class="right">EMA: 0.1, 0.19, 0.271 → 1. Velocity: 1, 1.9, 2.71 → 10 ✓</div>

## 🗣️ Say it out loud

"s t equals beta s t minus one, plus one minus beta times x t."

## 🤖 Where AI uses it

SGD with momentum, Adam's first and second moments (next lesson), the smoothed loss curve in TensorBoard/W&B, and EMA copies of weights used for diffusion models and some LLM checkpoints.

## 🎯 Your quest

1. `ema(values, beta)`: start at 0, return the list of averages after each value.
2. `momentum_step(theta, v, g, lr, beta)`: lists in, return `(new_theta, new_v)`.
3. `speedup(beta)`: 1 / (1 − β).

**Remember:** keep β of the old, blend in the new; agreeing gradients add up.

## Review

<details><summary>Safe learning rate for curvature 4?</summary>Below 0.5.</details>
<details><summary>What does f''(x) measure?</summary>Curvature: how fast the slope changes.</details>
