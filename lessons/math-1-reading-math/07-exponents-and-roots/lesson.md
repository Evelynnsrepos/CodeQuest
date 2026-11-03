---
title: Powers and roots
xp: 35
---
# Multiplying a number by itself

> **Warm-up:** one light switch has 2 positions. Two switches together have how many combinations? Three switches? Four?

**In one sentence:** a power says how many times to multiply a number by itself, and a root undoes that.

## 🪜 Plain words

Each extra switch **doubles** the number of combinations, because every old combination now comes in two versions (new switch off or on). Doubling again and again is "multiplying 2 by itself" many times. That's a **power**.

A **root** goes backwards: "what number, multiplied by itself, gives 9?" Answer: 3.

## 🪜 With numbers

- 1 switch: 2. 2 switches: 2 times 2 = 4. 3 switches: 2 times 2 times 2 = 8. 4 switches: 16.
- A computer **bit** is a switch, so 4 bits can store 16 different values, 8 bits 256.
- 3 times 3 = 9, so the square root of 9 is 3.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `2⁴` (small raised number) | "two to the four" / "two to the power of four" | 2 · 2 · 2 · 2 = 16 | `2 ** 4` |
| `x²` | "x squared" | x · x | `x ** 2` |
| `x³` | "x cubed" | x · x · x | `x ** 3` |
| `x^n` | "x to the n" | same as xⁿ, typed on a keyboard | `x ** n` |
| `√x` | "the square root of x" | the number that, squared, gives x | `math.sqrt(x)` |
| `x⁻¹` | "x to the minus one" | 1 divided by x | `x ** -1` |

The big number is the **base**, the small raised one is the **exponent** (how many copies).

## 🔬 Take the formula apart

How many values fit in b bits?

<div class="formula"><span class="k1">levels</span> = <span class="k2">2</span><sup><span class="k3">b</span></sup></div>

| Piece | Say it | Means | 4 bits |
|---|---|---|---|
| <span class="k1">levels</span> | "levels" | how many different values | 16 |
| <span class="k2">2</span> | "two" | the **base**: each bit has 2 options | 2 |
| <span class="k3">b</span> (small, raised) | "to the b" | the **exponent**: how many 2s to multiply | 4 → 2·2·2·2 |

The rules (each one is just counting how many copies get multiplied):

| Rule | Why | Example |
|---|---|---|
| <span class="k2">x</span><sup><span class="k3">a</span></sup> · <span class="k2">x</span><sup><span class="k4">b</span></sup> = <span class="k2">x</span><sup><span class="k3">a</span>+<span class="k4">b</span></sup> | a copies, then b more | 2³ · 2² = 2⁵ = 32 |
| (<span class="k2">x</span><sup><span class="k3">a</span></sup>)<sup><span class="k4">b</span></sup> = <span class="k2">x</span><sup><span class="k3">a</span>·<span class="k4">b</span></sup> | b groups of a copies | (2²)³ = 2⁶ = 64 |
| x⁰ = 1 | no copies: nothing changed, stays 1 | 7⁰ = 1 |
| x⁻ⁿ = 1 / xⁿ | negative = divide instead | 2⁻³ = 1/8 |
| x^(1/2) = √x | "half a multiplication" | 9^(1/2) = 3 |

## 🔀 What if the formula were different?

<div class="wrong"><b>levels = 2 · b</b> (times instead of power): 4 bits → 8 levels. Real 4-bit quantization has 16. You'd be off by half, and for 16 bits you'd say 32 instead of 65,536!</div>
<div class="wrong"><b>levels = b²</b> (base and exponent swapped): 4 bits → 16 (lucky!), but 8 bits → 64 instead of 256.</div>
<div class="right"><b>levels = 2ᵇ</b>: 16 for 4 bits, 256 for 8 bits ✓</div>

## 🗣️ Say it out loud

`2ᵇ` → "two to the b" → "the number of different patterns b bits can make".

## 🤖 Where AI uses it

Quantization (`2ᵇ` levels), squared errors `(y − ŷ)²`, attention's `√d`, learning rates like `3 · 10⁻⁴`, scaling laws `N^0.34`.

## 🎯 Your quest

1. `levels(bits)`: `2^bits`.
2. `power_rules_hold(x, a, b)`: return `True` if both `xᵃ · xᵇ == x^(a+b)` and `(xᵃ)ᵇ == x^(a·b)` (compare with `abs(...) < 1e-9`).
3. `rms(xs)`: the **root mean square**: square each number, take the average, then the square root.

**Remember:** a negative exponent means "divide", a ½ exponent means "square root".

## Review

<details><summary>What is |−7|?</summary>7.</details>
<details><summary>Why can't you just average raw errors?</summary>Positive and negative errors cancel out.</details>
