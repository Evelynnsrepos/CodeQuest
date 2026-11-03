---
title: Adding and scaling vectors
xp: 35
---
# Arrows you can stack and stretch

> **Warm-up:** you walk the arrow (3, 1), then the arrow (1, 2). Where do you end up?

**In one sentence:** add vectors entry by entry, and multiply a vector by a number by multiplying every entry.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `v + w` | "v plus w" | `(v₁ + w₁, v₂ + w₂, …)`; both must have the same dimension | `[a + b for a, b in zip(v, w)]` |
| `c·v` or `cv` | "c times v" | **scalar multiplication**: `(c·v₁, c·v₂, …)` | `[c * a for a in v]` |
| `v − w` | "v minus w" | `v + (−1)·w`: the arrow from w to v | |
| `a₁v₁ + a₂v₂ + …` | "a linear combination" | scale several vectors and add them | |

Careful: here `v₁, v₂` (with subscripts on a **bold** v) can mean "vector number 1, vector number 2", not entries. The text tells you which.

## The idea

- **Adding** = walking one arrow, then the other (tip to tail). `(3, 1) + (1, 2) = (4, 3)`.
- **Scaling** = stretching: `2·(3, 1) = (6, 2)` is twice as long, same direction. Negative numbers flip it around. `0.5` halves it.
- A **linear combination** mixes vectors with weights: `0.7·a + 0.3·b`. Most of a neural network is linear combinations.

Python warning: `[1, 2] + [3, 4]` is `[1, 2, 3, 4]` (gluing lists!), and `2 * [1, 2]` is `[1, 2, 1, 2]`. Math vectors need the loops above (NumPy and PyTorch arrays do it the math way).

## 🗣️ Say it out loud

`x + attention(x)` (a residual connection) → "x plus the attention output", entry by entry: the layer **adds** information to the token's vector.

## 🧮 Worked example

`0.5·(2, 4) + 2·(1, −1)`:

1. Scale: `(1, 2)` and `(2, −2)`
2. Add: `(1 + 2, 2 + (−2)) = (3, 0)`

## 🤖 Where AI uses it

Residual connections (`x + f(x)`), gradient descent (`θ − η·∇L`: a scaled vector subtracted), attention's output (a weighted sum of value vectors), the famous `king − man + woman ≈ queen` in word embeddings.

## 🎯 Your quest

1. `add(v, w)`
2. `scale(c, v)`
3. `lin_comb(coeffs, vectors)`: `Σᵢ coeffsᵢ · vectorsᵢ`.

**Remember:** vector math is entry by entry, and Python lists don't do it for you.

## Review

<details><summary>Python index of v₃?</summary>v[2].</details>
<details><summary>What does x ∈ ℝ⁷⁶⁸ tell you?</summary>x is a vector of 768 real numbers.</details>
