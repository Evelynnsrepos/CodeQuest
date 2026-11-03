---
title: Matrices: grids of numbers
xp: 35
---
# A table of numbers with a shape

> **Warm-up:** a tiny layer turns 3 inputs into 2 outputs, and each output has its own 3 weights. How would you write down all 6 weights neatly?

**In one sentence:** a matrix is a rectangle of numbers with rows and columns, and its shape (rows × columns) is the first thing to look at.

## 🪜 Plain words

A matrix is a spreadsheet of numbers. **Rows** go across, **columns** go down. To point at one number you say which row, then which column, like "row 2, seat 3" in a cinema. Always **row first**.

## 🪜 With numbers

```
        col 1  col 2  col 3
row 1 [   1      2      3  ]
row 2 [   4      5      6  ]
```

2 rows, 3 columns: shape "2 by 3". Row 2, column 3 holds 6. Column 3 is (3, 6).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `A` (capital) | "matrix A" | a grid | list of rows `[[1, 2, 3], [4, 5, 6]]` |
| `m × n` | "m by n" | m rows, n columns | `len(A)`, `len(A[0])` |
| `ℝᵐˣⁿ` | "R m by n" | all m × n grids of numbers | |
| `Aᵢⱼ` | "A i j" | row i, column j (from 1) | `A[i - 1][j - 1]` |

Convention: capital letter = matrix, bold small letter = vector, plain small letter = one number.

## 🔬 Take the formula apart

<div class="formula"><span class="k1">A</span> ∈ ℝ<sup><span class="k2">2</span>×<span class="k3">3</span></sup>, &nbsp; <span class="k1">A</span><sub><span class="k2">2</span><span class="k3">3</span></sub> = 6</div>

| Piece | Say it | Means |
|---|---|---|
| <span class="k1">A</span> | "A" | the matrix |
| ∈ ℝ | "is in R" | made of ordinary numbers |
| <span class="k2">2</span> × | "two by" | **2 rows** (always first) |
| <span class="k3">3</span> | "three" | **3 columns** |
| <span class="k1">A</span><sub><span class="k2">2</span><span class="k3">3</span></sub> | "A two three" | row 2, column 3 = 6 (Python `A[1][2]`) |

## 🔀 What if it were different?

<div class="wrong"><b>A₂₃ read as column 2, row 3</b>: there is no row 3 → error (or the wrong number in a bigger matrix).</div>
<div class="wrong"><b>A₂₃ as A[2][3]</b> (Python counting): also out of range. Subtract 1 from both.</div>
<div class="right"><b>A₂₃ = A[1][2] = 6</b> ✓</div>

## 🗣️ Say it out loud

`W ∈ ℝ^(d_out × d_in)` → "W is a d-out by d-in matrix" → "one row per output, one column per input."

## 🤖 Where AI uses it

Every layer's weights. A batch of 32 tokens × 4096 numbers is a 32 × 4096 matrix. Images are grids of pixels.

## 🎯 Your quest

Use math counting (from 1).

1. `shape(A)`: `(rows, columns)`.
2. `entry(A, i, j)`
3. `column(A, j)`

**Remember:** rows × columns, and row first.

## Review

<details><summary>Cosine similarity of (1, 0) and (0, 5)?</summary>0.</details>
<details><summary>What does cos⁻¹ mean?</summary>The reverse function (arc cosine), not 1/cos.</details>
