---
title: ∫: integrals as area
xp: 50
---
# Adding up infinitely thin strips

> **Warm-up:** you drive at 60 km/h for 2 hours. How far did you go? Now draw speed (up) against time (across). What shape is under the line, and what's its area?

**In one sentence:** the integral `∫` adds up a quantity over a range; on a graph it's the area under the curve, and you can get it by summing thin rectangles.

## 🪜 Plain words

Warm-up: 60 × 2 = 120 km. On the graph, that's a rectangle 2 wide and 60 tall: area 120. **Area under a speed curve = distance.**

If the speed changes, the shape isn't a rectangle. Trick: slice it into thin strips, treat each strip as a rectangle (height = curve value in the middle of the strip), and add them up. Thinner strips → closer to the true area. The limit of infinitely thin strips is the **integral**.

The integral is the **opposite** of the derivative: derivative = rate from amount, integral = amount from rate.

## 🪜 With numbers

f(x) = 2x from 0 to 3 (a triangle: ½ · 3 · 6 = **9**).

- 3 strips, width 1, middles at 0.5, 1.5, 2.5: heights 1, 3, 5. Sum: (1 + 3 + 5) · 1 = **9** ✓

f(x) = x² from 0 to 1 (true area **1/3 ≈ 0.333**):

- 2 strips of width 0.5, middles 0.25 and 0.75: (0.0625 + 0.5625) · 0.5 = 0.3125
- 1000 strips: 0.33333 ✓

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `∫` | "the integral" | a stretched S, for **S**um | a loop that adds |
| `∫ₐᵇ` | "integral from a to b" | add up from a to b (small numbers bottom and top) | `range` from a to b |
| `f(x)` | "f of x" | the height of the curve | `f(x)` |
| `dx` | "d x" | the (infinitely thin) strip width: says "x is the thing we slice along" | `width = (b - a) / n` |
| `Δx` | "delta x" | a real, non-tiny strip width | `width` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">∫</span><sub><span class="k2">a</span></sub><sup><span class="k3">b</span></sup> <span class="k4">f(x)</span> <span class="k5">dx</span> ≈ <span class="k1">Σ</span> <span class="k4">f(middleᵢ)</span> · <span class="k5">Δx</span></div>

| Piece | Say it | Means | 2x from 0 to 3, 3 strips |
|---|---|---|---|
| <span class="k1">∫</span> / <span class="k1">Σ</span> | "integral" / "sum" | add up the strips | |
| <span class="k2">a</span> | "from a" | start | 0 |
| <span class="k3">b</span> | "to b" | end | 3 |
| <span class="k4">f(x)</span> | "f of x" | strip height | 1, 3, 5 |
| <span class="k5">dx</span> / <span class="k5">Δx</span> | "d x" / "delta x" | strip width = (b − a) / n | 1 |
| total | | area | 9 |

## 🔀 What if it were different?

<div class="wrong"><b>Swap a and b</b> (∫ from 3 to 0): −9. Going backwards flips the sign.</div>
<div class="wrong"><b>Forget the width</b> (just add heights): with 6 strips of width 0.5 the heights add to 18. That counts each strip as 1 wide: double the true area.</div>
<div class="wrong"><b>Use left edges with 2 strips on x²</b>: (0 + 0.25) · 0.5 = 0.125 instead of ~0.333. Bad heights make a coarse sum badly wrong; middles are much better.</div>
<div class="right">Σ f(middle) · Δx → 9 for 2x, → 0.3333 for x² ✓</div>

## 🗣️ Say it out loud

`∫₀³ 2x dx = 9` → "the integral from 0 to 3 of 2x d x is 9."

## 🤖 Where AI uses it

**Probability** (Math 4): for continuous values, the probability of landing between a and b is the area under the density curve, and the total area must be 1. **AUC** (area under the ROC curve) scores classifiers: 1.0 perfect, 0.5 coin flip. Diffusion models (AI beyond LLMs) integrate a noise process over time.

## 🎯 Your quest

1. `riemann(f, a, b, n)`: midpoint sum with `n` strips.
2. `prob_between(density, a, b)`: `riemann(density, a, b, 1000)`.
3. `auc(points)`: area under a polyline given as sorted `(x, y)` points, using trapezoids: each piece is `(x₂ − x₁) · (y₁ + y₂) / 2`.

**Remember:** ∫ = sum of height × width, over thinner and thinner strips.

## Review

<details><summary>Backprop in five words?</summary>Forward and remember, backward multiply.</details>
<details><summary>∂a/∂z for a sigmoid?</summary>a(1 − a).</details>
