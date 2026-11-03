---
title: Fractions, ratios and percentages
xp: 25
---
# Parts of a whole

> **Warm-up:** your model file is 4.9 GB and your GPU has 12 GB. What fraction of the VRAM does it use, and what percentage is that?

**In one sentence:** a fraction is a division you haven't done yet, and a percentage is that division times 100.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `a/b` or `a` over `b` | "a over b" | a divided by b; `a` is the **numerator** (top), `b` the **denominator** (bottom) | `a / b` |
| `%` | "percent" | "out of 100": 25% = 25/100 = 0.25 | `* 100` to show, `/ 100` to use |
| `a : b` | "a to b" | a **ratio**: a compared to b | `a / b` |
| `≈` | "approximately" | roughly equal | `round(x, 2)` |

## The idea

- **Fraction → decimal:** divide. `3/4 = 0.75`.
- **Decimal → percent:** multiply by 100. `0.75 = 75%`.
- **Percent of something:** `20% of 50 = 0.20 · 50 = 10`.
- **Percent change:** `(new − old) / old · 100`. Positive = went up, negative = went down.
- **Dividing by a fraction** = multiplying by it flipped: `6 / (1/2) = 6 · 2 = 12`.

## 🗣️ Say it out loud

`(new − old) / old` → "how much it changed, compared to where it started."

## 🧮 Worked example

Your loss went from 2.5 to 1.5:

1. Change: `1.5 − 2.5 = −1.0`
2. Compare to start: `−1.0 / 2.5 = −0.4`
3. As a percentage: `−0.4 · 100 = −40%`, so the loss dropped by 40%.

## 🤖 Where AI uses it

VRAM use, accuracy (correct / total), win rates in evaluations (wins / games), and "bits per weight" (Q4_K_M ≈ 4.8 bits out of FP16's 16 ≈ 30% of the size).

## 🎯 Your quest

1. `as_percent(part, whole)`: `part / whole · 100`.
2. `percent_change(old, new)`.
3. `percent_of(p, x)`: `p` percent of `x`.

**Remember:** "percent" means "divided by 100".

## Review

<details><summary>Where does the invisible bracket go in a fraction?</summary>Around the whole top and the whole bottom.</details>
<details><summary>What is 2 + 3 · 4?</summary>14.</details>
