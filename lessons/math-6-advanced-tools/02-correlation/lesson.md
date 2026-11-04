---
title: Correlation: covariance without units
xp: 50
---
# How strong, from −1 to 1

> **Warm-up:** covariance was 18.75 for hours vs score. Is that a strong relationship? You can't tell. Why not?

**In one sentence:** correlation is covariance divided by both standard deviations, which removes the units and squeezes the result between −1 and 1.

## 🪜 Plain words

Covariance grows if you measure in minutes instead of hours (lesson 01). To compare fairly, measure each column **in its own standard deviations** first (z-scores, Math 4 lesson 08), then take the covariance. That's correlation, called **r**:

- **r = 1**: a perfect rising straight line.
- **r = −1**: a perfect falling line.
- **r ≈ 0**: no straight-line relationship (there might still be a curved one!).

## 🪜 With numbers

From lesson 01: cov = 18.75, sₓ = 1.581 (std of hours), s_y = 11.94 (std of scores).

r = 18.75 / (1.581 · 11.94) = 18.75 / 18.87 = **0.993**. Almost a perfect line.

Change hours to minutes: cov becomes 1125, sₓ becomes 94.87; r = 1125 / (94.87 · 11.94) = 0.993. **Same.** That's the point.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `r` | "r" | the correlation (Pearson's) | `statistics.correlation` |
| `sₓ` | "s x" | sample standard deviation of x | `statistics.stdev(xs)` |
| `cov(x, y)` | "covariance" | lesson 01 | |
| `/` | "divided by" | | `/` |
| `r²` | "r squared" | share of y's ups and downs a straight line explains | `r ** 2` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">r</span> = <span class="k2">cov(x, y)</span> / ( <span class="k3">sₓ</span> · <span class="k4">s_y</span> )</div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k2">cov(x, y)</span> | "covariance of x and y" | do they move together, in units | 18.75 |
| <span class="k3">sₓ</span> | "s x" | typical spread of hours | 1.581 |
| <span class="k4">s_y</span> | "s y" | typical spread of scores | 11.94 |
| <span class="k1">r</span> | "r" | unit-free strength, −1 to 1 | 0.993 |

## 🔀 What if it were different?

<div class="wrong"><b>Divide by only one std</b>: 18.75 / 1.581 = 11.86. Still has units (score points); not comparable.</div>
<div class="wrong"><b>Read r as "x causes y"</b>: ice-cream sales and drowning correlate strongly (both rise in summer). Correlation can come from a hidden third cause. Only an experiment (an A/B test) shows cause.</div>
<div class="wrong"><b>Read r ≈ 0 as "unrelated"</b>: y = x² for x = −2..2 gives r = 0 exactly, though y depends completely on x. r only sees straight lines.</div>
<div class="right">r = 18.75 / (1.581 · 11.94) = 0.993 ✓</div>

## 🗣️ Say it out loud

"r is the covariance of x and y over s x times s y."

## 🤖 Where AI uses it

Feature selection (drop one of two features with r ≈ 1), checking whether a cheap metric tracks human ratings (an LLM judge's score vs human scores: AI engineer 2 lesson 09), and spotting **spurious correlations** a model might learn (a "cow" classifier that really detects grass).

## 🎯 Your quest

1. `correlation(xs, ys)`: r, using your own covariance and sample standard deviations (`statistics.stdev` is fine).
2. `r_squared(xs, ys)`.
3. `most_correlated(columns, target)`: `columns` is a dict name → list; return the name whose **absolute** correlation with `target` is largest.

**Remember:** correlation is unit-free, linear-only, and not causation.

## Review

<details><summary>What does the diagonal of a covariance matrix hold?</summary>Each column's variance.</details>
