---
title: Matrix times vector
xp: 45
---
# A matrix is a machine for vectors

> **Warm-up:** two neurons. Neuron 1 has weights (1, 2), neuron 2 has weights (3, 4). The input is (5, 6). Compute both outputs (no bias).

**In one sentence:** to multiply a matrix by a vector, take the dot product of every row with the vector; one number per row comes out.

## 🪜 Plain words

Each **row** of the matrix is one neuron's weights. Each neuron does a dot product with the input. Stack all the answers into a new list. That's matrix times vector. A matrix with 2 rows always gives 2 numbers, whatever goes in: so a matrix can **change the size** of a vector.

## 🪜 With numbers

- Neuron 1: 1 times 5 + 2 times 6 = 5 + 12 = **17**.
- Neuron 2: 3 times 5 + 4 times 6 = 15 + 24 = **39**.
- Result: (17, 39).

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `Ax` | "A x" / "A times x" | dot product of every row of A with x | `[dot(row, x) for row in A]` |
| `(Ax)ᵢ` | "entry i of A x" | row i of A · x | |
| `Σⱼ Aᵢⱼ xⱼ` | "the sum over j of A i j x j" | that dot product, written out | |
| shape rule | | (m × **n**) times (**n**) gives (m) | |

## 🔬 Take the formula apart

<div class="formula">(<span class="k1">A</span><span class="k2">x</span>)<sub><span class="k3">i</span></sub> = <span class="k4">Σ</span><sub><span class="k5">j</span></sub> <span class="k1">A</span><sub><span class="k3">i</span><span class="k5">j</span></sub> <span class="k2">x</span><sub><span class="k5">j</span></sub></div>

| Piece | Say it | Means | Row i = 1 |
|---|---|---|---|
| (<span class="k1">A</span><span class="k2">x</span>)<sub><span class="k3">i</span></sub> | "entry i of A x" | output number i | 17 |
| <span class="k4">Σ</span><sub><span class="k5">j</span></sub> | "sum over j" | walk along the row, j = column number | j = 1, 2 |
| <span class="k1">A</span><sub><span class="k3">i</span><span class="k5">j</span></sub> | "A i j" | weight in row i, column j | 1, 2 |
| <span class="k2">x</span><sub><span class="k5">j</span></sub> | "x j" | input number j, times the weight | 5, 6 → 5 + 12 |

Notice: the **same j** sits on A and on x. That shared letter is the "multiply these together" instruction.

## 🔀 What if it were different?

<div class="wrong"><b>Using columns instead of rows</b>: (1·5 + 3·6, 2·5 + 4·6) = (23, 34). That's Aᵀx, a different machine.</div>
<div class="wrong"><b>Input of the wrong length</b> (3 numbers into a 2-column matrix): undefined. Each row needs exactly one input per column.</div>
<div class="right"><b>Row · x for each row</b>: (17, 39) ✓</div>

Some matrices do pure geometry: `[[0, −1], [1, 0]]` rotates any 2D arrow by 90°; `[[2, 0], [0, 2]]` doubles it.

## 🗣️ Say it out loud

`h = Wx` → "h equals W x" → "every output is the weighted sum of the inputs using that output's row."

## 🤖 Where AI uses it

Every linear layer, Q/K/V in attention, the MLP, LoRA. It's the most common operation in AI; GPUs exist to do it fast.

## 🎯 Your quest

1. `matvec(A, x)`: raise `ValueError` if the number of columns ≠ `len(x)`.
2. `rotate90(v)`: rotate a 2D vector 90° anticlockwise **using matvec** and `[[0, −1], [1, 0]]`.

**Remember:** one dot product per row.

## Review

<details><summary>Shape of [[1, 2, 3], [4, 5, 6]]?</summary>2 × 3.</details>
<details><summary>Python for A₂₁?</summary>A[1][0].</details>
