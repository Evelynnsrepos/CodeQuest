---
title: Eigenvectors: directions a matrix only stretches
xp: 50
---
# The special arrows

> **Warm-up:** the matrix `[[2, 0], [0, 1]]` stretches things sideways. Which arrows keep pointing in exactly the same direction after it?

**In one sentence:** an eigenvector is an arrow that a matrix only makes longer or shorter, never turns, and its eigenvalue says by how much.

## 🪜 Plain words

Stretch a rubber sheet sideways. Most arrows drawn on it **tilt** toward the sideways direction. But an arrow pointing exactly sideways just gets longer, and one pointing exactly up doesn't change at all. Those special directions are the **eigenvectors** ("eigen" is German for "own": the matrix's own directions).

**Power iteration**: start with any arrow and apply the matrix again and again (shrinking it back to length 1 each time). The strongest stretch direction wins and the arrow swings toward it.

## 🪜 With numbers

`[[2, 0], [0, 1]]`:

- (1, 0) → (2, 0): same direction, 2× longer. Eigenvector, stretch **2**.
- (0, 1) → (0, 1): unchanged. Eigenvector, stretch **1**.
- (1, 1) → (2, 1): tilted. Not an eigenvector.

## 🔣 The signs

| Sign | Say it | Means |
|---|---|---|
| `v` | "v" | the special arrow (eigenvector) |
| `λ` | "lambda" | the stretch factor (eigenvalue) |
| `Av = λv` | "A v equals lambda v" | A does nothing but stretch v by λ |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">A</span><span class="k2">v</span> = <span class="k3">λ</span><span class="k2">v</span></div>

| Piece | Say it | Means | A = [[2, 1], [1, 2]], v = (1, 1) |
|---|---|---|---|
| <span class="k1">A</span><span class="k2">v</span> | "A v" | the matrix applied to the arrow (matrix × vector) | (3, 3) |
| = | "equals" | is the same as | |
| <span class="k3">λ</span> | "lambda" | a plain number | 3 |
| <span class="k3">λ</span><span class="k2">v</span> | "lambda v" | the same arrow, just scaled | 3·(1, 1) = (3, 3) ✓ |

On the left a **matrix** acts on v; on the right just a **number** does. That only works for these special arrows.

## 🔀 What if it were different?

<div class="wrong"><b>v = (1, 0)</b> for [[2, 1], [1, 2]]: Av = (2, 1), which is not a multiple of (1, 0). It turned → not an eigenvector.</div>
<div class="wrong"><b>v = (0, 0)</b>: A·0 = λ·0 for every λ. The zero arrow has no direction, so it never counts.</div>
<div class="right">(1, 1) with λ = 3, and (1, −1) with λ = 1 ✓</div>

## 🗣️ Say it out loud

"A v equals lambda v" → "A only stretches v, by lambda."

## 🤖 Where AI uses it

**PCA** (directions of largest spread in data), **exploding/vanishing gradients** (repeatedly multiplying by a matrix with |λ| > 1 explodes, < 1 vanishes; that's the RNN problem), Google's original PageRank.

## 🎯 Your quest

`matvec`, `dot`, `norm` are given.

1. `is_eigenvector(A, v)`: compute `λ = (v·Av)/(v·v)`, then check every entry of `Av − λv` is within `1e-9` of 0.
2. `power_iteration(A, steps)`: start from all 1s, repeat `v ← Av / ‖Av‖`, return `(λ, v)` with `λ = v·Av`.

**Remember:** eigenvectors keep their direction; λ is the stretch.

## Review

<details><summary>det([[a, b], [c, d]])?</summary>ad − bc.</details>
<details><summary>What does det = 0 mean?</summary>The matrix squashes space flat: no inverse.</details>
