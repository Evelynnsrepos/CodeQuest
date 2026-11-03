---
title: Matrix times vector
xp: 45
---
# A matrix is a machine that transforms vectors

> **Warm-up:** with two rows of weights `(1, 2)` and `(3, 4)`, and an input `(5, 6)`, compute two neuron outputs (no bias). That's a matrix–vector product.

**In one sentence:** to multiply a matrix by a vector, take the dot product of every row with the vector; you get one number per row.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `Ax` | "A x" / "A times x" | the vector of `(row i of A) · x` for every row | `[dot(row, x) for row in A]` |
| `(Ax)ᵢ = Σⱼ Aᵢⱼxⱼ` | "entry i of A x is the sum over j of A i j times x j" | the same, as a formula | |
| `(m × n)(n) → (m)` | | the shape rule: **columns of A must equal length of x** | |

## The idea

```
[ 1  2 ]   [ 5 ]   [ 1·5 + 2·6 ]   [ 17 ]
[ 3  4 ] · [ 6 ] = [ 3·5 + 4·6 ] = [ 39 ]
```

- An `m × n` matrix takes an `n`-vector and returns an `m`-vector. So a matrix **changes the dimension**: 4096 → 14336 in an MLP.
- Geometrically, a matrix **transforms** space: it can rotate, stretch, squash or flip arrows. A **linear** transformation keeps straight lines straight and the origin fixed.

Examples in 2D:

| Matrix | Does |
|---|---|
| `[[2, 0], [0, 2]]` | doubles every vector |
| `[[0, −1], [1, 0]]` | rotates 90° anticlockwise |
| `[[1, 0], [0, −1]]` | mirrors (flips the y part) |

## 🗣️ Say it out loud

`h = Wx` → "h equals W times x" → "every output is a weighted sum of the inputs, using that output's row of weights".

## 🧮 Worked example

Rotate `(1, 0)` by 90°: `[[0, −1], [1, 0]] · (1, 0) = (0·1 + (−1)·0, 1·1 + 0·0) = (0, 1)`. East became north. ✓

## 🤖 Where AI uses it

Every linear layer, every Q/K/V projection in attention, the MLP's up and down matrices, LoRA's `BAx` (LLMs 6). It's the single most common operation in AI; GPUs exist to do it fast.

## 🎯 Your quest

`dot` is given.

1. `matvec(A, x)`: raise `ValueError` if the number of columns doesn't match `len(x)`.
2. `rotate90(v)`: rotate a 2D vector 90° anticlockwise **using `matvec`** and the rotation matrix above.

**Remember:** matrix × vector = one dot product per row.

## Review

<details><summary>What's the shape of [[1, 2, 3], [4, 5, 6]]?</summary>2 × 3 (2 rows, 3 columns).</details>
<details><summary>Python for A₂₁?</summary>A[1][0].</details>
