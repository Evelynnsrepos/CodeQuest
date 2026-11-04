---
title: Matrix times matrix
xp: 50
---
# Many matrix–vector products at once

> **Warm-up:** 32 tokens go through the same layer. Do you need 32 separate calculations, or is there one bigger one?

**In one sentence:** in `AB`, the number in row i, column j is "row i of A dot column j of B", and the two inside sizes must match.

## 🪜 Plain words

Put the 32 token vectors side by side as the **columns** of a matrix (or as rows, depending on the convention). Multiplying the weight matrix by this whole matrix runs every token through the layer at once. Each spot in the result is one dot product: one row from the left matrix with one column from the right one.

## 🪜 With numbers

```
[1 2]   [5 6]
[3 4] · [7 8]
```

- Row 1 · column 1: 1·5 + 2·7 = 19
- Row 1 · column 2: 1·6 + 2·8 = 22
- Row 2 · column 1: 3·5 + 4·7 = 43
- Row 2 · column 2: 3·6 + 4·8 = 50

Result `[[19, 22], [43, 50]]`.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `AB` | "A B" | matrix product | NumPy/PyTorch: `A @ B` |
| `(AB)ᵢⱼ` | "entry i j of A B" | row i of A · column j of B | |
| `(m × n)(n × p) = (m × p)` | "m by n times n by p gives m by p" | the **shape rule** | |
| FLOPs | "flops" | floating-point operations (multiplies + adds) | |

## 🔬 Take the formula apart

<div class="formula">(<span class="k1">A</span><span class="k2">B</span>)<sub><span class="k3">i</span><span class="k4">j</span></sub> = <span class="k5">Σ</span><sub><span class="k6">k</span></sub> <span class="k1">A</span><sub><span class="k3">i</span><span class="k6">k</span></sub> <span class="k2">B</span><sub><span class="k6">k</span><span class="k4">j</span></sub></div>

| Piece | Say it | Means | Entry (1, 2) |
|---|---|---|---|
| (<span class="k1">A</span><span class="k2">B</span>)<sub><span class="k3">i</span><span class="k4">j</span></sub> | "A B, row i column j" | one spot of the result | 22 |
| <span class="k5">Σ</span><sub><span class="k6">k</span></sub> | "sum over k" | walk along row i of A **and** down column j of B together | k = 1, 2 |
| <span class="k1">A</span><sub><span class="k3">i</span><span class="k6">k</span></sub> | "A i k" | row i of A | 1, 2 |
| <span class="k2">B</span><sub><span class="k6">k</span><span class="k4">j</span></sub> | "B k j" | column j of B | 6, 8 → 6 + 16 = 22 |

The shape rule:

<div class="formula">(<span class="k1">m</span> × <span class="k6">n</span>) · (<span class="k6">n</span> × <span class="k2">p</span>) = (<span class="k1">m</span> × <span class="k2">p</span>)</div>

The two inner sizes (n) must be equal (that's k's range); the outer two give the result's shape. Cost: ≈ **2·m·n·p** FLOPs.

## 🔀 What if it were different?

<div class="wrong"><b>BA instead of AB</b>: [[23, 34], [31, 46]]. Different! Order matters for matrices (unlike normal numbers).</div>
<div class="wrong"><b>Multiplying position by position</b> ([[1·5, 2·6], [3·7, 4·8]] = [[5, 12], [21, 32]]): that's ⊙ (lesson 10), not a matrix product.</div>
<div class="wrong"><b>(2 × 3) · (2 × 3)</b>: inner sizes 3 and 2 don't match: undefined.</div>
<div class="right"><b>AB</b> = [[19, 22], [43, 50]] ✓</div>

## 🗣️ Say it out loud

`Y = XW` → "Y equals X W" → "send every row of X through W at once."

## 🤖 Where AI uses it

Batches, attention (`QKᵀ`, then `·V`), LoRA (`BA`). Over 90% of an LLM's compute.

## 🎯 Your quest

1. `can_multiply(shape_a, shape_b)`
2. `matmul(A, B)`: raise `ValueError` if shapes don't fit.
3. `matmul_flops(m, n, p)`: `2·m·n·p`.

**Remember:** inner sizes must match; outer sizes are the result.

## Review

<details><summary>What does [[0, −1], [1, 0]] do?</summary>Rotates a 2D arrow 90° anticlockwise.</details>
<details><summary>(m × n) times an n-vector gives…</summary>An m-vector.</details>
