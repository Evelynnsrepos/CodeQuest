---
title: Curvature and the biggest safe learning rate
xp: 55
---
# Why a learning rate can be "too big"

> **Warm-up:** in Math 3 lesson 10, learning rate 0.1 worked and 1.1 blew up on the loss (w − 3)². Where exactly is the border, and why?

**In one sentence:** the second derivative measures how sharply a loss curves, and gradient descent on a bowl is only stable when learning rate < 2 ÷ curvature.

## 🪜 Plain words

- The first derivative is the **slope** (Math 3).
- The **second derivative** is how fast the slope itself changes: the **curvature**. A narrow, steep valley has big curvature; a wide, gentle one has small curvature.
- A loss shaped like a bowl everywhere (curvature never negative) is **convex**: it has one bottom and no traps.

Each gradient step jumps by learning rate × slope. In a sharp valley the slope grows fast as you move, so a big step flies past the bottom and lands higher on the other side. The border is **2 ÷ curvature**: exactly at it, you bounce back and forth forever; above it, each bounce gets bigger.

## 🪜 With numbers

L(w) = (w − 3)². Slope 2(w − 3). Curvature **2** everywhere. Safe if η < 2/2 = **1**.

| η | first steps from w = 0 | result |
|---|---|---|
| 0.1 | 0.6, 1.08, 1.46… | slowly to 3 ✓ |
| 0.5 | 3 | lands exactly on the bottom in one step |
| 1.0 | 6, 0, 6, 0… | bounces forever |
| 1.1 | 6.6, −1.32, 8.18… | explodes |

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `f''(x)` | "f double prime of x" | second derivative: the slope of the slope | `second_derivative(f, x)` |
| `d²f/dx²` | "d two f, d x squared" | same thing | |
| `η` | "eta" | learning rate (Math 3) | `lr` |
| `<` | "less than" | | `<` |
| convex | | bowl-shaped: f'' ≥ 0 everywhere | |
| `H` | "the Hessian" | all second derivatives of a many-input function (a matrix) | |

## 🔬 Take the formulas apart

<div class="formula"><span class="k1">f''(x)</span> ≈ ( <span class="k2">f(x + h)</span> − <span class="k3">2 f(x)</span> + <span class="k4">f(x − h)</span> ) / <span class="k5">h²</span></div>

| Piece | Say it | Means | (w − 3)² at w = 0, h = 1 |
|---|---|---|---|
| <span class="k2">f(x + h)</span> | "f of x plus h" | one step right | 4 |
| <span class="k3">2 f(x)</span> | "two f of x" | twice the middle | 18 |
| <span class="k4">f(x − h)</span> | "f of x minus h" | one step left | 16 |
| / <span class="k5">h²</span> | "over h squared" | per step, squared (two derivatives deep) | (4 − 18 + 16)/1 = 2 |

<div class="formula"><span class="k6">η</span> &lt; 2 / <span class="k1">curvature</span></div>

## 🔀 What if it were different?

<div class="wrong"><b>η &lt; 1 / curvature as the limit</b>: too cautious by half. Safe, but up to 2× slower than needed.</div>
<div class="wrong"><b>η &lt; 2 / slope</b> (first derivative): the slope is 0 at the bottom, so the "limit" would be infinite exactly where overshooting happens.</div>
<div class="wrong"><b>Second difference with + 2f(x)</b>: (4 + 18 + 16)/1 = 38. Nonsense curvature.</div>
<div class="right">curvature 2 → η must be below 1 ✓</div>

## 🗣️ Say it out loud

"f double prime of x is about f of x plus h, minus two f of x, plus f of x minus h, all over h squared."

## 🤖 Where AI uses it

Neural network losses are **not** convex, but near a good point they look like bowls with very different curvatures in different directions. The sharpest direction sets the safe learning rate: that's why warmup and learning-rate schedules exist (LLMs 8), and why Adam (lesson 10) rescales each weight separately.

## 🎯 Your quest

1. `second_derivative(f, x, h=1e-4)`.
2. `max_stable_lr(curvature)`: 2 / curvature.
3. `is_convex(f, xs)`: `True` if the second derivative is ≥ −1e-6 at every x in `xs`.

**Remember:** sharper bowl → smaller safe steps; limit 2 ÷ curvature.

## Review

<details><summary>Gradient of softmax + cross-entropy?</summary>p − y.</details>
<details><summary>Sum of that gradient's entries?</summary>0.</details>
