---
title: Big and tiny numbers: scientific notation
xp: 30
---
# Writing 8,000,000,000 without counting zeros

> **Warm-up:** "Llama 3 8B was trained on 15T tokens with a learning rate of 3e-4." What do `8B`, `15T` and `3e-4` mean as plain numbers?

**In one sentence:** scientific notation writes a number as "a few digits times 10 to some power", so you can see its size at a glance.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `3 · 10⁴` | "three times ten to the four" | 30,000 | `3e4` |
| `3 · 10⁻⁴` | "three times ten to the minus four" | 0.0003 | `3e-4` |
| `3e-4` | "three e minus four" | same thing, computer style | `3e-4` |
| K, M, B, T | thousand, million, billion, trillion | 10³, 10⁶, 10⁹, 10¹² | `1e3`, `1e6`, `1e9`, `1e12` |
| `~` or `≈` | "about" | roughly | |

## The idea

The exponent counts how many places the decimal point moves:

- Positive: move **right** (bigger). `7.2 · 10⁹ = 7,200,000,000`.
- Negative: move **left** (smaller). `3 · 10⁻⁴ = 0.0003`.

Multiplying: **multiply the front numbers, add the exponents**. `(2 · 10⁹) · (3 · 10¹²) = 6 · 10²¹`.

An **order of magnitude** is one power of 10. "Two orders of magnitude bigger" means about 100 times bigger.

Careful: storage uses **GB = 10⁹ bytes**, while **GiB = 2³⁰ ≈ 1.074 · 10⁹** bytes. Tools mix them up; the difference is about 7%.

## 🗣️ Say it out loud

`6 · N · D` with N = 8·10⁹, D = 1.5·10¹³ → "six times eight billion times fifteen trillion" → `7.2 · 10²³` FLOPs.

## 🧮 Worked example

Size of an 8B model in FP16 (2 bytes per weight):

1. `8 · 10⁹ · 2 = 16 · 10⁹` bytes
2. In GB, divide by `10⁹`: **16 GB**

## 🤖 Where AI uses it

Parameter counts, token counts, FLOPs, learning rates (`1e-5` to `1e-3`), tiny epsilons like `1e-8` in Adam.

## 🎯 Your quest

1. `human(n)`: write a number with a suffix and one decimal: `"8.0B"`, `"15.0T"`, `"124.4M"`, `"3.5K"`; below 1000, just `str(n)`. Use T for ≥ 10¹², B for ≥ 10⁹, M for ≥ 10⁶, K for ≥ 10³.
2. `model_gb(params, bytes_per_param)`: size in GB (10⁹ bytes).

**Remember:** `e` in a number like `3e-4` means "times ten to the".

## Review

<details><summary>What is 2⁻¹?</summary>½ = 0.5.</details>
<details><summary>How many values fit in 8 bits?</summary>2⁸ = 256.</details>
