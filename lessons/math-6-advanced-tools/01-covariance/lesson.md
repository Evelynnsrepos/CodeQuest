---
title: Covariance: do two things move together?
xp: 50
---
# Up together, down together

> **Warm-up:** when you study more hours, does your test score tend to go up? How would you put a number on "tend to"?

**In one sentence:** covariance is the average of "how far x is from its mean" times "how far y is from its mean": positive if they rise together, negative if one rises while the other falls, near 0 if there's no pattern.

## 🪜 Plain words

Take each person. Ask two questions: are they **above or below average** in hours? Above or below average in score?

- Above in both, or below in both → their product is **positive**: a vote for "together".
- Above in one, below in the other → the product is **negative**: a vote for "opposite".

Average all the votes. That's covariance.

## 🪜 With numbers

| Hours x | Score y | x − 3 (mean 3) | y − 64 (mean 64) | product |
|---|---|---|---|---|
| 1 | 50 | −2 | −14 | 28 |
| 2 | 55 | −1 | −9 | 9 |
| 3 | 65 | 0 | 1 | 0 |
| 4 | 70 | 1 | 6 | 6 |
| 5 | 80 | 2 | 16 | 32 |

Sum of products = 75. Divide by n − 1 = 4 (a sample, like the sample standard deviation in Math 4 lesson 11): **covariance = 18.75**. Positive: they move together.

With **many** features (say 3 columns), compute it for every pair. The result is a table, the **covariance matrix**: entry (i, j) is the covariance of column i and column j. Its diagonal holds each column's variance (a column's covariance with itself).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `x̄` | "x bar" | the mean of x | `sum(xs) / len(xs)` |
| `Σ` | "sum" | add up over all items i | `sum(...)` |
| `(xᵢ − x̄)` | "x i minus x bar" | how far item i is from the mean | `x - mx` |
| `n − 1` | "n minus one" | sample correction (Bessel) | `len(xs) - 1` |
| `cov(x, y)` | "covariance of x and y" | the result | `statistics.covariance` |
| `Σ` (bold, a matrix) | "sigma" | the covariance matrix (same letter, different job!) | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">cov(x, y)</span> = <span class="k2">Σ</span> <span class="k3">(xᵢ − x̄)</span> · <span class="k4">(yᵢ − ȳ)</span> / <span class="k5">(n − 1)</span></div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k3">(xᵢ − x̄)</span> | "x i minus x bar" | above (+) or below (−) average hours | −2, −1, 0, 1, 2 |
| <span class="k4">(yᵢ − ȳ)</span> | "y i minus y bar" | above or below average score | −14, −9, 1, 6, 16 |
| · | "times" | the vote: + if same side, − if opposite | 28, 9, 0, 6, 32 |
| <span class="k2">Σ</span> | "sum" | add all votes | 75 |
| <span class="k5">(n − 1)</span> | "n minus one" | average them (sample version) | 4 |
| <span class="k1">cov(x, y)</span> | "covariance" | the result | 18.75 |

## 🔀 What if it were different?

<div class="wrong"><b>Forget to subtract the means</b>: Σ x·y / 4 = (50 + 110 + 195 + 280 + 400) / 4 = 258.75. Huge and positive even for unrelated data, because both columns are just positive numbers.</div>
<div class="wrong"><b>Add instead of multiply</b>: Σ ((x − x̄) + (y − ȳ)) = 0 always. Deviations from the mean always sum to zero, so you learn nothing.</div>
<div class="wrong"><b>Read the size as strength</b>: measure hours in minutes and the covariance becomes 60 × 18.75 = 1125, but the relationship didn't change. Covariance depends on units; lesson 02 fixes that.</div>
<div class="right">cov = 75 / 4 = 18.75: positive, they rise together ✓</div>

## 🗣️ Say it out loud

"Covariance is the sum of x i minus x bar times y i minus y bar, over n minus one."

## 🤖 Where AI uses it

PCA (lesson 04) starts from the covariance matrix. Adam's second moment (Math 5) is a diagonal of a covariance. Gaussian models, Kalman filters and "whitening" image features all use it, and so does the idea of *redundant features*: two columns with large covariance carry overlapping information.

## 🎯 Your quest

1. `covariance(xs, ys)`: the sample covariance.
2. `cov_matrix(columns)`: `columns` is a list of equal-length lists; return the matrix (list of rows) where entry `[i][j]` is `covariance(columns[i], columns[j])`.

**Remember:** same side of the mean → positive vote; average the votes.

## Review

<details><summary>Why divide by n − 1 for a sample?</summary>The sample's own mean sits closer to the data than the true mean, so dividing by n underestimates the spread.</details>
