---
title: Variance and standard deviation (σ)
xp: 50
---
# How spread out is it?

> **Warm-up:** two models both average 70% on a benchmark. One scores 69, 70, 71 on three runs; the other 40, 70, 100. Which do you trust more? Why?

**In one sentence:** variance is the average squared distance from the mean, and the standard deviation σ is its square root: the typical distance from the average, in the original units.

## 🪜 Plain words

The average alone hides how **wobbly** things are. To measure wobble:

1. Find the average.
2. For each value, how far is it from the average?
3. **Square** those distances (so negatives don't cancel positives, and big misses count extra).
4. Average the squares → **variance**.
5. Square-root it, to get back to normal units → **standard deviation**.

## 🪜 With numbers

Model A: 69, 70, 71. Mean 70. Distances −1, 0, 1. Squares 1, 0, 1. Variance 2/3 ≈ 0.67. σ ≈ **0.82**.

Model B: 40, 70, 100. Mean 70. Distances −30, 0, 30. Squares 900, 0, 900. Variance 600. σ ≈ **24.5**.

Same average, wildly different reliability.

Die: mean 3.5, variance 2.917, σ ≈ **1.71**.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `μ` | "mu" | the mean (lesson 06) | `mu` |
| `Var(X)` or `σ²` | "variance of X" / "sigma squared" | average squared distance from μ | `variance(d)` |
| `σ` | "sigma" (small sigma, again!) | standard deviation = √variance | `math.sqrt(var)` |
| `(x − μ)²` | "x minus mu, squared" | squared distance from the mean | `(x - mu) ** 2` |
| `√` | "square root" | (Math 1) | `math.sqrt` |

Small σ has three jobs in AI math: sigmoid σ(x), standard deviation σ, and the noise level in diffusion. The context tells you which.

## 🔬 Take the formula apart

<div class="formula"><span class="k1">σ²</span> = <span class="k2">E</span>[ ( <span class="k3">X</span> − <span class="k4">μ</span> )<span class="k5">²</span> ] &nbsp;&nbsp;&nbsp; <span class="k6">σ</span> = √<span class="k1">σ²</span></div>

| Piece | Say it | Means | Model B |
|---|---|---|---|
| <span class="k4">μ</span> | "mu" | the average | 70 |
| <span class="k3">X</span> − <span class="k4">μ</span> | "X minus mu" | each value's distance from it | −30, 0, 30 |
| ( … )<span class="k5">²</span> | "squared" | make positive, punish big misses | 900, 0, 900 |
| <span class="k2">E</span>[ … ] | "the expected value of" | average them (lesson 06) | 600 |
| <span class="k1">σ²</span> | "variance" | in squared units (points²) | 600 |
| <span class="k6">σ</span> | "sigma" | back to points | 24.5 |

## 🔀 What if it were different?

<div class="wrong"><b>No square, just E[X − μ]</b>: (−30 + 0 + 30)/3 = 0. Always exactly 0 for any data: distances above and below cancel.</div>
<div class="wrong"><b>Forget the square root</b>: "model B is off by 600 points". Wrong units; on a 0–100 scale that's nonsense.</div>
<div class="wrong"><b>Distance from 0 instead of from μ</b>: E[X²] = 5500 for model B. That measures how big the numbers are, not how spread out.</div>
<div class="right">σ² = 600, σ ≈ 24.5 ✓</div>

## 🗣️ Say it out loud

"Sigma squared is the expected value of X minus mu, squared."

## 🤖 Where AI uses it

**LayerNorm/RMSNorm** (LLMs 8) divide by σ to keep activations at a steady size. Weight initialisation picks σ carefully (too big → explode, too small → vanish). Adam (Math 5) divides by a running σ of the gradients. Benchmark results should always come with ± σ.

## 🎯 Your quest

1. `variance(d)`: for a distribution dict `{value: prob}`.
2. `std(d)`.
3. `data_std(xs)`: σ of a plain list (each value equally likely; divide by n).

**Remember:** variance = average squared distance from the mean; σ = its root.

## Review

<details><summary>E[X] for a die?</summary>3.5.</details>
<details><summary>Is E[X²] the same as (E[X])²?</summary>No. For a die 15.17 vs 12.25.</details>
