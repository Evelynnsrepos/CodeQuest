---
title: Derivatives of eˣ, ln x and σ
xp: 50
---
# The three curves AI loves

> **Warm-up:** eˣ grows faster and faster. How fast is it growing at any moment? Guess before reading.

**In one sentence:** eˣ is its own slope, ln x has slope 1/x, and the sigmoid's slope is σ·(1 − σ): three facts used in nearly every neural network.

## 🪜 Plain words

- **eˣ** is magic: at every point, its slope **equals its own value**. When it's 20, it's growing by 20 per step. (That's why e is the special number, Math 1 lesson 15.)
- **ln x** (natural log, the undo of eˣ): its slope is 1 divided by x. Steep near 0, flatter and flatter for big x.
- **σ (sigmoid)** squeezes any number into 0..1. Its slope is biggest in the middle (0.25 at x = 0) and almost **zero** at both far ends, where the curve goes flat.

## 🪜 With numbers

| x | eˣ | slope of eˣ | ln x | slope of ln x | σ(x) | slope of σ |
|---|---|---|---|---|---|---|
| 0 | 1 | 1 | — | — | 0.5 | 0.25 |
| 1 | 2.718 | 2.718 | 0 | 1 | 0.731 | 0.197 |
| 4 | 54.6 | 54.6 | 1.386 | 0.25 | 0.982 | 0.018 |

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `e` | "e" | ≈ 2.718, the natural growth number | `math.e` |
| `eˣ` or `exp(x)` | "e to the x" | e multiplied by itself x times | `math.exp(x)` |
| `ln x` | "natural log of x" / "lon x" | which power of e gives x | `math.log(x)` |
| `σ(x)` | "sigma of x" (small sigma, not Σ!) | sigmoid: 1 / (1 + e⁻ˣ) | `1 / (1 + math.exp(-x))` |
| `σ'(x)` | "sigma prime of x" | slope of the sigmoid | |

## 🔬 Take the formulas apart

<div class="formula">d/dx <span class="k1">eˣ</span> = <span class="k1">eˣ</span> &nbsp;&nbsp;&nbsp; d/dx <span class="k2">ln x</span> = <span class="k3">1 / x</span></div>

<div class="formula"><span class="k4">σ'(x)</span> = <span class="k5">σ(x)</span> · ( <span class="k6">1 − σ(x)</span> )</div>

| Piece | Say it | Means | At x = 4 |
|---|---|---|---|
| <span class="k1">eˣ</span> = <span class="k1">eˣ</span> | "e to the x is its own derivative" | slope equals value | 54.6 |
| <span class="k3">1 / x</span> | "one over x" | slope of ln | 0.25 |
| <span class="k5">σ(x)</span> | "sigma of x" | the output, between 0 and 1 | 0.982 |
| <span class="k6">1 − σ(x)</span> | "one minus sigma of x" | how far the output is from 1 | 0.018 |
| <span class="k4">σ'(x)</span> | "sigma prime" | their product: the slope | 0.982 · 0.018 = 0.0177 |

The product is big only when **both** parts are medium. At the ends one part is nearly 0, so the slope is nearly 0.

## 🔀 What if it were different?

<div class="wrong"><b>σ'(x) = σ(x) · σ(x)</b>: at x = 0 it gives 0.25 (looks right by coincidence!) but at x = 4 it gives 0.964 instead of 0.018. You'd think the flat end is steep.</div>
<div class="wrong"><b>σ'(x) = σ(x) · (1 + σ(x))</b>: at x = 0: 0.75 instead of 0.25. Every gradient through a sigmoid would be 3× too big.</div>
<div class="wrong"><b>d/dx ln x = ln x</b> (copying the eˣ rule): at x = 1 gives 0, but ln is clearly rising there with slope 1.</div>
<div class="right">eˣ → eˣ, ln x → 1/x, σ → σ(1 − σ) ✓</div>

## 🗣️ Say it out loud

"Sigma prime of x equals sigma of x times one minus sigma of x."

## 🤖 Where AI uses it

The **vanishing gradient problem**: at x = 4 the sigmoid passes on only 1.8% of the signal. Stack many sigmoids and the learning signal dies, which is why modern networks use ReLU/GELU inside and keep sigmoid for outputs and gates. `ln` appears in every loss (log-probabilities, Math 5), and its 1/x slope is why a confident wrong answer (p tiny) produces a huge gradient.

## 🎯 Your quest

1. `sigmoid(x)`.
2. `d_sigmoid(x)`: σ(x)·(1 − σ(x)).
3. `d_ln(x)`: 1/x.
4. `d_exp(x)`: eˣ.

**Remember:** eˣ is its own slope; ln's slope is 1/x; sigmoid's slope is σ(1 − σ).

## Review

<details><summary>Derivative of 4x³?</summary>12x².</details>
<details><summary>Derivative of a plain number like 9?</summary>0.</details>
