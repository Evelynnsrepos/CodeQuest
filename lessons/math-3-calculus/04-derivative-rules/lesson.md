---
title: Shortcut rules: power, sum, constant
xp: 45
---
# Derivatives without limits

> **Warm-up:** last lesson, the slope of x² at x = 3 was 6. At x = 5 it would be 10. Spot a pattern?

**In one sentence:** a few simple rules give you the derivative of a formula directly, no tiny steps needed: bring the power down in front, lower the power by one.

## 🪜 Plain words

Doing the h-shrinking trick for every formula is slow. Mathematicians found shortcuts:

- **Power rule:** for x to some power, put the power **in front** as a multiplier, then make the power **one smaller**. x² → 2x. x³ → 3x².
- **Number in front stays:** 5·x² → 5·2x = 10x.
- **Plain number alone** (like + 7) disappears: it never changes, so its slope is 0.
- **Plus stays plus:** do each part separately and add.

## 🪜 With numbers

3x² + 5x + 7, piece by piece:

- 3x² → 3 · 2 · x¹ = **6x**
- 5x (that's 5x¹) → 5 · 1 · x⁰ = 5 · 1 = **5** (anything to the power 0 is 1)
- 7 → **0**

Derivative: **6x + 5**. At x = 2: 6·2 + 5 = **17**. (Check with lesson 03's `central_diff`: you'd get 17.000…)

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `xⁿ` | "x to the n" | x multiplied by itself n times (Math 1) | `x ** n` |
| `n` | "n" | the power (exponent) | |
| `c` | "c" | a constant: a fixed number in front | |
| `d/dx` | "d by d x" | "take the derivative of" | |
| `x⁰` | "x to the zero" | always 1 | `x ** 0 == 1` |

## 🔬 Take the formula apart

<div class="formula">d/dx ( <span class="k1">c</span> · x<sup><span class="k2">n</span></sup> ) = <span class="k1">c</span> · <span class="k2">n</span> · x<sup><span class="k3">n − 1</span></sup></div>

| Piece | Say it | Means | For 3x² |
|---|---|---|---|
| d/dx ( … ) | "d by d x of" | the slope of what's inside | |
| <span class="k1">c</span> | "c" | the number in front: it **stays** | 3 |
| <span class="k2">n</span> (up high) | "to the n" | the power… | 2 |
| <span class="k2">n</span> (down in front) | "times n" | …comes **down** as a multiplier | 3 · 2 = 6 |
| x<sup><span class="k3">n − 1</span></sup> | "x to the n minus one" | the power drops by **one** | x¹ = x |
| result | | | 6x |

Plus two small rules: d/dx (**number**) = 0, and d/dx (A + B) = A' + B'.

## 🔀 What if it were different?

<div class="wrong"><b>Bring n down but forget to lower the power</b>: 3x² → 6x². At x = 2 that says 24, but the true slope is 12. Your weights would move twice as far as they should.</div>
<div class="wrong"><b>Lower the power but forget to bring n down</b>: 3x² → 3x. At x = 2: 6 instead of 12.</div>
<div class="wrong"><b>Keep the + 7</b>: 6x + 5 + 7. At x = 2: 24 instead of 17. A constant shifts the curve up, but doesn't make it steeper.</div>
<div class="right">3x² + 5x + 7 → 6x + 5, at x = 2 → 17 ✓</div>

## 🗣️ Say it out loud

`d/dx x³ = 3x²` → "d by d x of x cubed is three x squared."

## 🤖 Where AI uses it

The squared error `(prediction − target)²` is a power-2 thing, so its derivative is `2 · (prediction − target)`: that's the signal that trains every regression model. The "2" comes straight from the power rule.

## 🎯 Your quest

A polynomial is stored as a list of numbers in front: `[7, 5, 3]` means 7 + 5x + 3x² (position = power).

1. `evaluate(coeffs, x)`: the value at x.
2. `derive(coeffs)`: the derivative as a new list (`[7, 5, 3]` → `[5, 6]`).

**Remember:** power comes down, power goes one down; constants vanish.

## Review

<details><summary>What does f'(x) mean?</summary>The slope of f at x: how much the output moves per tiny nudge of the input.</details>
<details><summary>Central difference formula?</summary>(f(x + h) − f(x − h)) / 2h.</details>
