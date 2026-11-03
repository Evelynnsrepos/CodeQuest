---
title: Matrices: grids of numbers
xp: 35
---
# A table of numbers with a shape

> **Warm-up:** a small neural layer turns 3 inputs into 2 outputs. Each output has its own 3 weights. How would you store all 6 weights?

**In one sentence:** a matrix is a rectangle of numbers with m rows and n columns, and its shape (m × n) is the most important thing about it.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `A` (capital, often bold) | "matrix A" | a grid of numbers | list of rows: `[[1, 2, 3], [4, 5, 6]]` |
| `A ∈ ℝᵐˣⁿ` | "A is m by n" | m rows, n columns | `len(A)`, `len(A[0])` |
| `Aᵢⱼ` or `A[i, j]` | "A i j" | the entry in **row i, column j** (from 1) | `A[i - 1][j - 1]` |
| `Aᵢ,:` | "row i of A" | a whole row | `A[i - 1]` |
| `A:,ⱼ` | "column j of A" | a whole column | `[row[j - 1] for row in A]` |

**Row first, then column**, always: "**R**oman **C**atholic", "**R**C cola", whatever helps you remember.

## The idea

```
        col 1  col 2  col 3
row 1 [   1      2      3  ]
row 2 [   4      5      6  ]        A ∈ ℝ²ˣ³,  A₂₃ = 6
```

- Capital letters are matrices, small bold letters vectors, plain small letters numbers. That convention alone helps read papers.
- A vector is a matrix with one column (n × 1) or one row (1 × n).
- Shapes in AI are big: Llama 3 8B's attention matrix `W_Q` is 4096 × 4096 (16.8 million numbers).

## 🗣️ Say it out loud

`W ∈ ℝ^(d_out × d_in)` → "W is a d-out by d-in matrix" → one row per output, one column per input.

## 🧮 Worked example

`A = [[1, 2, 3], [4, 5, 6]]`: shape 2 × 3, `A₁₂ = 2`, row 2 = `(4, 5, 6)`, column 3 = `(3, 6)`.

## 🤖 Where AI uses it

Every layer's weights are a matrix. A **batch** of 32 token vectors of size 4096 is a 32 × 4096 matrix. Images are matrices of pixels (Math 2 lesson 14 and AI beyond LLMs).

## 🎯 Your quest

Use math counting (from 1) for `i` and `j`.

1. `shape(A)`: `(rows, columns)`.
2. `entry(A, i, j)`
3. `column(A, j)`

**Remember:** shape is rows × columns, and indices go row first.

## Review

<details><summary>Cosine similarity of (1, 0) and (0, 5)?</summary>0: they're perpendicular.</details>
<details><summary>What does cos⁻¹ mean?</summary>The inverse function (arc cosine), not 1/cos.</details>
