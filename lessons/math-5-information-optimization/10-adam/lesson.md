---
title: Adam: the optimizer almost everyone uses
xp: 70
---
# Momentum plus a personal step size for every weight

> **Warm-up:** one weight gets gradients around 500, another around 0.001. With one learning rate for both, what goes wrong?

**In one sentence:** Adam keeps a moving average of each weight's gradient (direction) and of its squared gradient (typical size), corrects their start-up bias, and steps by "average direction ÷ typical size", so every weight moves about the learning rate per step.

## 🪜 Plain words

With plain gradient descent, the weight with gradient 500 jumps wildly and the one with 0.001 barely moves. Adam fixes that per weight:

1. **m**: EMA of the gradient (lesson 09): which way, smoothed.
2. **v**: EMA of the gradient **squared**: how big gradients usually are.
3. **Bias correction:** both start at 0, so early on they're too small (lesson 09's 0.1, 0.19…). Divide by (1 − βᵗ) to fix it.
4. **Step:** m̂ / √v̂. Direction divided by typical size → roughly ±1, whatever the gradient scale. Times the learning rate.
5. **ε** (tiny, like 10⁻⁸) on the bottom so we never divide by 0.

## 🪜 With numbers

First step (t = 1), β₁ = 0.9, β₂ = 0.999, gradient g = 0.5, lr = 0.001:

- m = 0.1 · 0.5 = 0.05 → m̂ = 0.05 / (1 − 0.9) = **0.5**
- v = 0.001 · 0.25 = 0.00025 → v̂ = 0.00025 / (1 − 0.999) = **0.25**
- step = 0.001 · 0.5 / √0.25 = **0.001**

With g = 500 instead: m̂ = 500, v̂ = 250,000, √v̂ = 500 → step **0.001** again. Same size, whatever the scale.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `m` | "m" | first moment: average gradient | `m` |
| `v` | "v" | second moment: average squared gradient | `v` |
| `β₁`, `β₂` | "beta one", "beta two" | their EMA factors (0.9, 0.999) | `b1, b2` |
| `βᵗ` | "beta to the t" | β multiplied by itself t times | `b1 ** t` |
| `m̂`, `v̂` | "m hat", "v hat" | bias-corrected versions | |
| `ε` | "epsilon" | tiny safety number | `eps = 1e-8` |
| `g²` | "g squared" | element by element | `g * g` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">m</span> ← β₁m + (1 − β₁)<span class="k5">g</span> &nbsp; <span class="k2">v</span> ← β₂v + (1 − β₂)<span class="k5">g²</span> &nbsp; <span class="k3">m̂ = m / (1 − β₁ᵗ)</span> &nbsp; <span class="k3">v̂ = v / (1 − β₂ᵗ)</span></div>

<div class="formula"><span class="k4">θ</span> ← <span class="k4">θ</span> − <span class="k6">η</span> · <span class="k3">m̂</span> / ( √<span class="k3">v̂</span> + ε )</div>

| Piece | Say it | Means | g = 0.5, t = 1 |
|---|---|---|---|
| <span class="k1">m</span> | "m" | smoothed direction | 0.05 |
| <span class="k2">v</span> | "v" | smoothed squared size | 0.00025 |
| <span class="k3">/ (1 − βᵗ)</span> | "over one minus beta to the t" | undo the start-at-zero bias; fades out as t grows | ÷ 0.1, ÷ 0.001 |
| <span class="k3">m̂</span> / √<span class="k3">v̂</span> | "m hat over root v hat" | direction ÷ typical size ≈ ±1 | 0.5 / 0.5 = 1 |
| <span class="k6">η</span> | "eta" | learning rate | 0.001 |
| <span class="k4">θ</span> ← | "theta becomes" | update | θ − 0.001 |

## 🔀 What if it were different?

<div class="wrong"><b>No bias correction</b>: m / √v = 0.05 / 0.0158 = 3.16 → the first steps are 3× too big, right when the model is most fragile.</div>
<div class="wrong"><b>No square root</b>: m̂ / v̂ = 0.5 / 0.25 = 2, and for g = 500 it's 500 / 250,000 = 0.002. Step size depends on scale again; the whole point is lost.</div>
<div class="wrong"><b>No ε</b>: a weight whose gradient has always been 0 has v̂ = 0 → 0 / 0 = NaN.</div>
<div class="wrong"><b>β₂ = 0.9 instead of 0.999</b>: v reacts too fast; one rare large gradient makes steps unstable. (Some LLM recipes use 0.95, a deliberate middle ground.)</div>
<div class="right">first step = lr · sign(g) = 0.001 for g = 0.5 and for g = 500 ✓</div>

## 🗣️ Say it out loud

"Theta becomes theta minus eta times m hat over root v hat plus epsilon."

## 🤖 Where AI uses it

AdamW (Adam + weight decay, next lesson) trains almost every LLM. Its memory cost explains LLMs 8: m and v are two extra FP32 numbers per weight, so full fine-tuning with Adam needs about 16 bytes per parameter.

## 🎯 Your quest

`adam_step(theta, g, m, v, t, lr=1e-3, b1=0.9, b2=0.999, eps=1e-8)`: all of `theta, g, m, v` are lists, `t` starts at 1. Return `(new_theta, new_m, new_v)`.

**Remember:** direction ÷ typical size, bias-corrected, times lr.

## Review

<details><summary>EMA update?</summary>s ← β s + (1 − β) x.</details>
<details><summary>Momentum's long-run speed-up with β = 0.9?</summary>10×.</details>
