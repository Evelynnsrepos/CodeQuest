---
title: Matrix times matrix
xp: 50
---
# Many matrix–vector products at once

> **Warm-up:** you have 32 tokens, each a vector, and one weight matrix. Do you have to loop over the tokens one by one?

**In one sentence:** in `AB`, entry (i, j) is the dot product of row i of A with column j of B, and the inner sizes must match.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `AB` | "A B" / "A times B" | matrix product | `matmul(A, B)` (NumPy: `A @ B`) |
| `(AB)ᵢⱼ = Σₖ AᵢₖBₖⱼ` | "entry i j of A B is the sum over k of A i k times B k j" | row i of A · column j of B | |
| `(m × n)(n × p) = (m × p)` | "m by n times n by p gives m by p" | the **shape rule** | |
| `@` | "at" / "matmul" | Python's matrix-multiply operator (NumPy/PyTorch) | `A @ B` |

## The idea

**The shape rule** is the one thing to check first, always:

```
  (m × n) · (n × p)  =  (m × p)
       └──┘ must match
```

The two inner numbers must be equal; the outer two give the result's shape.

```
[1 2]   [5 6]   [1·5+2·7  1·6+2·8]   [19 22]
[3 4] · [7 8] = [3·5+4·7  3·6+4·8] = [43 50]
```

Important facts:

- **Order matters:** `AB ≠ BA` in general. (`BA` might not even have a valid shape.)
- **Brackets don't:** `(AB)C = A(BC)`. So several layers in a row can be multiplied into one matrix (that's why we need non-linear activations in between).
- **Cost:** an `(m × n)(n × p)` product needs `m·n·p` multiplications and about as many additions: **≈ 2·m·n·p FLOPs**.

## 🗣️ Say it out loud

`Y = XWᵀ` → "Y equals X times W transpose" → "send every row of X (every token) through the layer W at once."

## 🧮 Worked example

Shapes: `X` is 32 × 4096 (32 tokens), `W` is 4096 × 1024. `XW` is `32 × 1024`, and costs `2 · 32 · 4096 · 1024 ≈ 268 million` FLOPs.

## 🤖 Where AI uses it

Batches (all tokens at once), attention (`QKᵀ`, then `·V`), LoRA (`BA`). Matrix multiplication is >90% of the compute in an LLM.

## 🎯 Your quest

1. `can_multiply(shape_a, shape_b)`: shapes are `(rows, cols)` tuples.
2. `matmul(A, B)`: raise `ValueError` if the shapes don't fit.
3. `matmul_flops(m, n, p)`: `2·m·n·p`.

**Remember:** inner sizes must match, outer sizes are the result.

## Review

<details><summary>What does [[0, −1], [1, 0]] do to a 2D vector?</summary>Rotates it 90° anticlockwise.</details>
<details><summary>An m × n matrix times an n-vector gives a vector of which length?</summary>m.</details>
