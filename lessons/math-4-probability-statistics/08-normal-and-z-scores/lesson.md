---
title: The normal curve and z-scores
xp: 55
---
# The bell curve, and "how unusual is this?"

> **Warm-up:** adults average 170 cm, give or take about 10 cm. Is 185 cm unusual? Is 210 cm? How would you put a number on "unusual"?

**In one sentence:** the normal distribution is the bell-shaped curve that shows up whenever many small random effects add up, and a z-score says how many standard deviations a value is from the mean.

## 🪜 Plain words

Lots of things cluster around an average, with fewer and fewer cases further out: heights, measurement errors, the sum of many dice. That shape is the **bell curve**, or **normal distribution**. It is fully described by two numbers: its middle (μ) and its width (σ).

A **z-score** converts any value into "how many σ's away from the middle". That lets you compare things on different scales.

The famous rule: about **68%** of values fall within 1σ, **95%** within 2σ, **99.7%** within 3σ.

## 🪜 With numbers

Heights: μ = 170, σ = 10.

- 185 cm: (185 − 170) / 10 = **z = 1.5**. Tall, not rare (about 7% are taller).
- 210 cm: (210 − 170) / 10 = **z = 4**. Extremely rare (about 3 in 100,000).
- 160 cm: **z = −1**. Negative z = below average.

Standardising a whole list (subtract the mean, divide by σ): `[2, 4, 4, 4, 5, 5, 7, 9]` (μ = 5, σ = 2) → `[−1.5, −0.5, −0.5, −0.5, 0, 0, 1, 2]`.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `N(μ, σ²)` | "normal with mean mu and variance sigma squared" | the bell curve with that centre and width (note: the 2nd number is σ², not σ!) | `random.gauss(mu, sigma)` |
| `X ∼ N(0, 1)` | "X is standard normal" | centre 0, width 1 | |
| `z` | "z" / "z-score" | distance from the mean in σ's | `(x - mu) / sigma` |
| `p(x)` | "the density at x" | height of the curve (not a probability by itself; area is, Math 3 lesson 12) | |
| `π` | "pi" (here really 3.14159…) | | `math.pi` |
| `exp(…)` | "e to the" | (Math 1) | `math.exp` |

## 🔬 Take the formulas apart

<div class="formula"><span class="k1">z</span> = ( <span class="k2">x</span> − <span class="k3">μ</span> ) / <span class="k4">σ</span></div>

| Piece | Say it | Means | 185 cm |
|---|---|---|---|
| <span class="k2">x</span> | "x" | the value | 185 |
| − <span class="k3">μ</span> | "minus mu" | distance from the middle | 15 |
| / <span class="k4">σ</span> | "over sigma" | measured in standard deviations | 1.5 |

<div class="formula"><span class="k5">p(x)</span> = <span class="k6">1 / (σ√(2π))</span> · exp( <span class="k5">−</span> <span class="k1">z²</span> / 2 )</div>

| Piece | Means | At x = μ (z = 0), σ = 1 |
|---|---|---|
| <span class="k1">z²</span> | squared distance in σ's: the further out, the bigger | 0 |
| exp( <span class="k5">−</span> … / 2 ) | turns distance into height: e⁰ = 1 in the middle, tiny far out | 1 |
| <span class="k6">1 / (σ√(2π))</span> | scaling so the total area is exactly 1 | 0.399 |

## 🔀 What if it were different?

<div class="wrong"><b>Divide by σ² (variance) instead of σ</b>: (185 − 170) / 100 = 0.15. Everyone looks perfectly average.</div>
<div class="wrong"><b>Forget to subtract μ</b>: 185 / 10 = 18.5. Every height looks impossibly extreme.</div>
<div class="wrong"><b>exp(+z²/2)</b> (no minus): the curve grows instead of shrinking away from the middle; the area becomes infinite.</div>
<div class="wrong"><b>Read N(0, 4) as σ = 4</b>: it's σ² = 4, so σ = 2. You'd think it's twice as wide as it is.</div>
<div class="right">z = 1.5 for 185 cm; p(0) = 0.399 for N(0, 1) ✓</div>

## 🗣️ Say it out loud

"z equals x minus mu, over sigma."

## 🤖 Where AI uses it

**LayerNorm** is literally a z-score of each token's vector (then scaled). Weights are initialised from N(0, σ²). **Diffusion** models add normal noise, then learn to remove it (AI beyond LLMs). Anomaly detection flags |z| > 3.

## 🎯 Your quest

1. `z_score(x, mu, sigma)`.
2. `normal_pdf(x, mu, sigma)`.
3. `standardize(xs)`: z-score every value using the list's own mean and σ (divide by n).

**Remember:** z = how many σ's from the mean; 68/95/99.7.

## Review

<details><summary>Variance in words?</summary>The average squared distance from the mean.</details>
<details><summary>Why square the distances?</summary>So distances above and below don't cancel to 0.</details>
