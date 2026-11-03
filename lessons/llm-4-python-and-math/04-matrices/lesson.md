---
title: Matrices and matrix multiplication
xp: 40
---
# The operation LLMs are made of

> **Warm-up:** in the last lesson's `Linear` class, each output was a dot product of one weight row with the input. What do you get if you stack all those rows into one grid?

A **matrix** is a grid of numbers: `m` rows by `n` columns, written `m × n`. In Python, a list of rows:

```python
W = [[1, 2, 3],
     [4, 5, 6]]      # 2 × 3
```

**Matrix × vector** is exactly your `Linear` layer without the bias: each output is a row of `W` dotted with `x`. A 2 × 3 matrix turns a 3-vector into a 2-vector. Geometrically, a matrix is a *transformation* of space: it can rotate, stretch, squash and project (3Blue1Brown's *Essence of Linear Algebra*, chapter 3, shows this beautifully).

**Matrix × matrix**: `C = A @ B` where entry `C[i][j]` is row `i` of `A` dotted with column `j` of `B`:

```
A: m × k      B: k × n      C: m × n
          ↑ the inner sizes must match
```

That shape rule is the single most common source of errors in ML code ("mat1 and mat2 shapes cannot be multiplied (4x3 and 4x2)"). Read every error like that as: the inner numbers didn't match.

Why it's everywhere: a whole **batch** of token vectors stacked as rows, `X` (tokens × d), goes through a layer as `X @ Wᵀ`: one big matrix multiplication, which is exactly what GPUs are built to do fast. Q, K and V for all tokens are three matmuls; the attention scores are `Q @ Kᵀ`; the MLP is two or three more.

The **transpose** `Aᵀ` swaps rows and columns: `Aᵀ[j][i] = A[i][j]`.

## Your quest

1. `transpose(A)`.
2. `matmul(A, B)`: raise `ValueError("shape mismatch")` if the number of columns of `A` isn't the number of rows of `B`; otherwise return `C`.
3. `shape(A)`: return `(rows, columns)`.

Hint for `matmul`: the columns of `B` are the rows of `transpose(B)`.

## Review

<details><summary>What does RMSNorm do to a vector?</summary>Divides it by its root mean square (then scales by learned weights), keeping vector sizes stable through the layers.</details>
<details><summary>What does the dot product measure, geometrically?</summary>|a|·|b|·cos(angle): how strongly the vectors point the same way.</details>
