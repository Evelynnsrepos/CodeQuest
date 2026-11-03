---
title: Exponents and roots
xp: 35
---
# Repeated multiplication, and undoing it

> **Warm-up:** a 4-bit number can store how many different values? What about 8 bits?

**In one sentence:** an exponent says how many times to multiply a number by itself, and a root undoes that.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `xⁿ` or `x^n` | "x to the n" / "x to the power of n" | x multiplied by itself n times | `x ** n` |
| `x²` | "x squared" | `x · x` | `x ** 2` |
| `x³` | "x cubed" | `x · x · x` | `x ** 3` |
| `√x` | "the square root of x" | the number that squared gives x: `√9 = 3` | `math.sqrt(x)` or `x ** 0.5` |
| `x⁻¹` | "x to the minus one" | `1 / x` | `x ** -1` |

In `xⁿ`, `x` is the **base** and `n` the **exponent** (or power).

## The idea

`2⁴ = 2 · 2 · 2 · 2 = 16`. The rules all follow from "count the multiplications":

| Rule | Why | Example |
|---|---|---|
| `xᵃ · xᵇ = xᵃ⁺ᵇ` | a copies then b more copies | `2³ · 2² = 2⁵ = 32` |
| `(xᵃ)ᵇ = xᵃᵇ` | b groups of a copies | `(2²)³ = 2⁶ = 64` |
| `x⁰ = 1` | multiplying by nothing leaves 1 | `7⁰ = 1` |
| `x⁻ⁿ = 1 / xⁿ` | negative = divide | `2⁻³ = 1/8` |
| `x^(1/2) = √x` | half a multiplication | `9^(1/2) = 3` |

## 🗣️ Say it out loud

`2ᵇ` → "two to the b" → "the number of different patterns b bits can make."

## 🧮 Worked example

How many values can 4 bits hold? Each bit doubles the options: `2 · 2 · 2 · 2 = 2⁴ = 16`. So a 4-bit quantized weight can only be one of 16 levels (LLMs 2).

`√(1 / 128)` (attention scaling with d = 128): `1 / √128 ≈ 1 / 11.31 ≈ 0.088`.

## 🤖 Where AI uses it

Quantization levels (`2ᵇ`), squared errors (`(y − ŷ)²`), attention's `√d`, learning rates like `3 · 10⁻⁴`, and the scaling-law formula `A / N^0.34`.

## 🎯 Your quest

1. `levels(bits)`: `2^bits`.
2. `power_rules_hold(x, a, b)`: return `True` if both `xᵃ · xᵇ == x^(a+b)` and `(xᵃ)ᵇ == x^(a·b)` are true (compare with `abs(...) < 1e-9`).
3. `rms(xs)`: the **root mean square**: square each number, take the mean, then the square root.

**Remember:** a negative exponent means "divide", a ½ exponent means "square root".

## Review

<details><summary>What is |−7|?</summary>7.</details>
<details><summary>Why do raw errors need an absolute value or a square before averaging?</summary>Otherwise positive and negative errors cancel out.</details>
