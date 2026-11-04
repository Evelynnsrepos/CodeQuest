---
title: Outliers: mistake or real?
xp: 55
---
# The 99,999 € coffee

> **Warm-up:** prices in a café's sales file: 3.20, 2.90, 3.50, 3.10, 99999, 3.30. What happened in row 5?

An **outlier** is a value far from the rest. It can be:

- a **mistake** (a test order, a typo, a missing value coded as 99999, cents instead of euros), so fix or drop it;
- or **real and important** (a fraud, a viral day, a sensor fault you need to know about), so keep it and maybe study it.

So the rule is: **flag** outliers automatically, then **look** before deleting.

## The IQR fence

A robust way to flag them uses **quartiles**: sort the numbers and cut them into four equal groups.

- **Q1** = the value a quarter of the way up, **Q3** = three quarters of the way up.
- **IQR** ("inter-quartile range") = Q3 − Q1: how wide the middle half is.
- **Fences**: anything below Q1 − 1.5·IQR or above Q3 + 1.5·IQR is flagged.

<svg viewBox="0 0 520 120" width="100%" style="max-width:520px" role="img" aria-label="Box plot: a box from Q1 to Q3 with the median inside, whiskers out to the fences, and one dot far to the right marked outlier">
  <line x1="40" y1="60" x2="480" y2="60" stroke="currentColor" opacity=".25"/>
  <line x1="90" y1="45" x2="90" y2="75" stroke="currentColor" stroke-width="2"/>
  <line x1="90" y1="60" x2="170" y2="60" stroke="currentColor" stroke-width="2"/>
  <rect x="170" y="40" width="110" height="40" rx="4" fill="#6c4cf5" fill-opacity=".25" stroke="#6c4cf5" stroke-width="2"/>
  <line x1="220" y1="40" x2="220" y2="80" stroke="#6c4cf5" stroke-width="3"/>
  <line x1="280" y1="60" x2="360" y2="60" stroke="currentColor" stroke-width="2"/>
  <line x1="360" y1="45" x2="360" y2="75" stroke="currentColor" stroke-width="2"/>
  <circle cx="465" cy="60" r="7" fill="#e5484d"/>
  <text x="170" y="100" font-size="13" fill="currentColor" text-anchor="middle">Q1</text>
  <text x="220" y="30" font-size="13" fill="currentColor" text-anchor="middle">median</text>
  <text x="280" y="100" font-size="13" fill="currentColor" text-anchor="middle">Q3</text>
  <text x="90" y="100" font-size="13" fill="currentColor" text-anchor="middle">low fence</text>
  <text x="360" y="100" font-size="13" fill="currentColor" text-anchor="middle">high fence</text>
  <text x="465" y="40" font-size="13" fill="#e5484d" text-anchor="middle">outlier</text>
</svg>

Why not "more than 3 standard deviations from the mean" (z-scores, Math 4 lesson 08)? Because the outlier itself inflates the mean and standard deviation, so a huge value can hide itself. Quartiles barely move.

## Python you need

```python
import statistics
q1, q2, q3 = statistics.quantiles([3.2, 2.9, 3.5, 3.1, 99999, 3.3], n=4)
```

`quantiles(..., n=4)` returns the three cut points Q1, median, Q3.

## Your quest

1. `fences(xs, k=1.5)`: `(low, high)` = `(Q1 − k·IQR, Q3 + k·IQR)` using `statistics.quantiles(xs, n=4)`.
2. `outliers(xs, k=1.5)`: the **indexes** of values outside the fences.
3. `z_outliers(xs, limit=3)`: indexes where `abs(x − mean) / pstdev > limit` (to see it fail on the warm-up data).

**Remember:** flag automatically, decide by looking.

## Review

<details><summary>Why does checking near-duplicates matter for AI evaluation?</summary>A near-copy of a test question in the training data makes the test score look better than the model really is.</details>
