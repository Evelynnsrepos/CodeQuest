---
title: Determinant, inverse and solving equations
xp: 50
---
# Undoing a matrix

> **Warm-up:** `3x = 12`. How do you find x? Now: a matrix A turned x into b. How would you get x back?

**In one sentence:** the inverse `A⁻¹` undoes A, it exists only when the determinant isn't 0, and it lets you solve `Ax = b`.

## 🔣 New symbols

| Symbol | Say it | Means |
|---|---|---|
| `det(A)` or `|A|` | "the determinant of A" | one number: how much A scales area (2D) or volume |
| `A⁻¹` | "A inverse" | the matrix with `A⁻¹A = AA⁻¹ = I` |
| `Ax = b` | "A x equals b" | a system of linear equations |
| `x = A⁻¹b` | "x equals A inverse b" | its solution |
| singular | | `det(A) = 0`: no inverse |

## The idea

For a 2 × 2 matrix `A = [[a, b], [c, d]]`:

```
det(A) = a·d − b·c

A⁻¹ = 1/det(A) · [[ d, −b],
                  [−c,  a]]        (swap a and d, negate b and c)
```

- `det = 0` means A **squashes** the plane onto a line (rank < 2): information is lost, so it can't be undone.
- Two equations `2x + y = 5`, `x + 3y = 10` are `[[2, 1], [1, 3]] · (x, y) = (5, 10)`.
- In practice nobody computes inverses of big matrices (slow and unstable); solvers do it smarter. But `A⁻¹` appears in formulas all the time.

## 🗣️ Say it out loud

`w = (XᵀX)⁻¹ Xᵀ y` → "w equals the inverse of X transpose X, times X transpose y" → the exact best-fit line (linear regression's normal equation).

## 🧮 Worked example

`A = [[2, 1], [1, 3]]`: `det = 2·3 − 1·1 = 5`. `A⁻¹ = (1/5)·[[3, −1], [−1, 2]] = [[0.6, −0.2], [−0.2, 0.4]]`. Solve with `b = (5, 10)`: `x = 0.6·5 − 0.2·10 = 1`, `y = −0.2·5 + 0.4·10 = 3`. Check: `2·1 + 3 = 5` ✓, `1 + 3·3 = 10` ✓.

## 🤖 Where AI uses it

Linear regression, Gaussian distributions (inverse covariance), second-order optimizers, and understanding why a layer that collapses dimensions loses information.

## 🎯 Your quest

1. `det2(A)`
2. `inverse2(A)`: raise `ValueError` if the matrix is singular.
3. `solve2(A, b)`: `A⁻¹b`.

**Remember:** det 0 = squashed = no inverse.

## Review

<details><summary>How many parameters does LoRA with r = 8 add to a 1000 × 1000 matrix?</summary>8·1000 + 8·1000 = 16,000.</details>
<details><summary>What's the rank of [[1, 2], [2, 4]]?</summary>1: the second row is twice the first.</details>
