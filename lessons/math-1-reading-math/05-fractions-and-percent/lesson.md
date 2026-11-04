---
title: Fractions, ratios and percentages
xp: 25
---
# Parts of a whole

> **Warm-up:** your model file is 4.9 GB and your GPU has 12 GB. Roughly what part of the GPU's memory does it use? Half? A third? Less?

**In one sentence:** a fraction is a division you haven't done yet, and a percentage is that division times 100.

## 🪜 Plain words

A pizza cut into 4 slices; you eat 3. You ate "3 out of 4" slices. That's a **fraction**: three quarters. If you do the division you get a decimal, 0.75. "Percent" means "out of 100": 0.75 of something is 75 out of every 100, so **75%**.

## 🪜 With numbers

- 4.9 GB out of 12 GB: 4.9 divided by 12 is about 0.41, which is **41%**.
- 20% of 50: 20% is 0.20, and 0.20 times 50 is **10**.
- Loss went from 2.5 to 1.5: it changed by 1.5 minus 2.5 = −1.0; compared to the start that's −1.0 divided by 2.5 = −0.4, so **−40%** (it dropped by 40%).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `a/b` or `a` over `b` with a line | "a over b" | a divided by b. Top = **numerator**, bottom = **denominator** | `a / b` |
| `%` | "percent" | "out of 100": 25% = 0.25 | `* 100` to show, `/ 100` to use |
| `a : b` | "a to b" | a **ratio**: a compared to b | `a / b` |
| `≈` | "approximately" | roughly equal | `round(x, 2)` |

## 🔬 Take the formula apart

**Percent change:**

<div class="formula"><span class="k1">(new − old)</span> <span class="k2">/ old</span> <span class="k3">· 100</span></div>

| Piece | Say it | Means | Loss example (2.5 → 1.5) |
|---|---|---|---|
| <span class="k1">(new − old)</span> | "new minus old, in brackets" | how much it changed (do this first!) | 1.5 − 2.5 = −1.0 |
| <span class="k2">/ old</span> | "divided by old" | compare that change to where you started | −1.0 / 2.5 = −0.4 |
| <span class="k3">· 100</span> | "times a hundred" | turn the decimal into a percentage | −0.4 · 100 = −40% |

**Percent of something:**

<div class="formula"><span class="k1">p</span> <span class="k2">/ 100</span> <span class="k3">· x</span></div>

| Piece | Say it | Means | Example (20% of 50) |
|---|---|---|---|
| <span class="k1">p</span> | "p" | the percentage | 20 |
| <span class="k2">/ 100</span> | "over a hundred" | turns 20 into 0.20 | 0.2 |
| <span class="k3">· x</span> | "times x" | of this amount | 0.2 · 50 = 10 |

## 🔀 What if the formula were different?

<div class="wrong"><b>(new − old) / new · 100</b> (divided by the wrong one): −1.0 / 1.5 · 100 = −67%. You'd report a much bigger drop than really happened.</div>
<div class="wrong"><b>(old − new) / old · 100</b> (swapped): +40%. Same size, but it says the loss went <i>up</i>.</div>
<div class="wrong"><b>new − old / old · 100</b> (brackets missing): 1.5 − (2.5 / 2.5 · 100) = 1.5 − 100 = −98.5. Nonsense.</div>
<div class="right"><b>(new − old) / old · 100</b>: −40%, the loss dropped by 40% ✓</div>

## 🗣️ Say it out loud

`(new − old) / old · 100` → "new minus old, divided by old, times a hundred" → "how much it changed compared to where it started, in percent."

## 🤖 Where AI uses it

VRAM use, accuracy (correct ÷ total), win rates (wins ÷ games), "Q4 is about 30% of the FP16 size".

## 🎯 Your quest

1. `as_percent(part, whole)`: `part / whole · 100`.
2. `percent_change(old, new)`.
3. `percent_of(p, x)`: `p` percent of `x`.

**Remember:** "percent" means "divided by 100".

## Review

<details><summary>Where does the invisible bracket go in a fraction?</summary>Around the whole top and the whole bottom.</details>
<details><summary>Solve 4x + 2 = 10.</summary>x = 2.</details>
