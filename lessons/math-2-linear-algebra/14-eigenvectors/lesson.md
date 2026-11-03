---
title: Eigenvectors: directions a matrix only stretches
xp: 50
---
# The special arrows

> **Warm-up:** apply `[[2, 0], [0, 1]]` to the arrows (1, 0), (0, 1) and (1, 1). Which ones keep pointing the same way?

**In one sentence:** an eigenvector of A is a direction that A only stretches (by its eigenvalue λ) without turning.

## 🔣 New symbols

| Symbol | Say it | Means |
|---|---|---|
| `Av = λv` | "A v equals lambda v" | v is an **eigenvector**, λ its **eigenvalue** |
| `λ` | "lambda" | the stretch factor (negative = flipped, 0 = squashed) |
| power iteration | | repeat `v ← Av / ‖Av‖`; v turns toward the biggest eigenvector |
| Rayleigh quotient `vᵀAv / vᵀv` | | estimates λ from a (unit) eigenvector |

## The idea

Most arrows get rotated by a matrix. A few special ones only get longer or shorter. For `[[2, 0], [0, 1]]`: `(1, 0)` → `(2, 0)`, stretched by 2 (λ = 2); `(0, 1)` → `(0, 1)` (λ = 1); `(1, 1)` → `(2, 1)`: turned, so not an eigenvector.

**Power iteration:** start with any vector and keep applying A, normalizing each time. The direction with the biggest |λ| grows fastest and takes over. Then `λ ≈ v · Av` (with ‖v‖ = 1).

Why AI cares:

- **PCA** (AI beyond LLMs): the eigenvectors of the data's covariance matrix are the directions of largest variance.
- **Exploding/vanishing gradients:** if a recurrent weight matrix has |λ| > 1, repeated multiplication explodes; < 1, it vanishes (RNNs!).
- Google's original **PageRank** is the top eigenvector of the link matrix, found by power iteration.

## 🗣️ Say it out loud

`Av = λv` → "A times v equals lambda times v" → "A only stretches v by lambda."

## 🧮 Worked example

`A = [[2, 1], [1, 2]]`, `v = (1, 1)`: `Av = (3, 3) = 3·(1, 1)`. So (1, 1) is an eigenvector with λ = 3. And `(1, −1)` → `(1, −1)`: λ = 1.

## 🎯 Your quest

`matvec`, `dot` and `norm` are given.

1. `is_eigenvector(A, v)`: `True` if `Av` is a multiple of `v` (v not zero). Check that `Av − (λ)v` is ~0 using `λ = (v·Av)/(v·v)`, within `1e-9` per entry.
2. `power_iteration(A, steps)`: start from `[1.0, 1.0, …]` (length of A), repeat `v ← Av/‖Av‖` `steps` times, return `(λ, v)` with `λ = v·Av`.

**Remember:** eigenvectors keep their direction; λ says by how much they stretch.

## Review

<details><summary>det([[a, b], [c, d]]) = ?</summary>ad − bc.</details>
<details><summary>What does det = 0 mean?</summary>The matrix squashes space (loses a dimension), so it has no inverse.</details>
