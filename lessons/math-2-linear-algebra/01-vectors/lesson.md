---
title: Vectors: lists of numbers with meaning
xp: 30
---
# A vector is a list with a direction

> **Warm-up:** describe a flat with three numbers. Which numbers would you choose? Congratulations: that's a vector.

**In one sentence:** a vector is an ordered list of numbers, and you can picture it as an arrow from the origin to a point.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `v` (bold **v** or `v⃗`) | "vector v" | a list of numbers; bold or an arrow marks "this is a vector, not one number" | `v = [3, 1, 2]` |
| `vᵢ` | "v sub i" | entry number i (counting from **1**) | `v[i - 1]` |
| `v ∈ ℝⁿ` | "v is in R n" | v has n real numbers: its **dimension** is n | `len(v) == n` |
| `(3, 1, 2)` or a column | "the vector three, one, two" | written out | `[3, 1, 2]` |
| `0` (bold) | "the zero vector" | all zeros | `[0] * n` |

## The idea

Two ways to see the same thing:

- **A list of features:** a flat = `(size, rooms, floor) = (65, 3, 2)`. Order matters: `(3, 65, 2)` would mean something else.
- **An arrow:** `(3, 2)` is an arrow 3 steps right and 2 steps up. In 3D you need 3 numbers; in 4096D you can't picture it, but all the math works the same.

**Dimension** = how many numbers. A single number is called a **scalar** (it "scales" vectors, next lesson).

Papers often write vectors as **columns** (stacked vertically). It's the same list; the direction only matters for matrix shapes (lesson 6).

## 🗣️ Say it out loud

`x ∈ ℝ⁴⁰⁹⁶` → "x is a vector of 4096 real numbers" → one token's hidden state in Llama 3 8B.

## 🧮 Worked example

`v = (4, −1, 7)`: dimension 3; `v₁ = 4` (Python `v[0]`), `v₃ = 7` (Python `v[2]`).

## 🤖 Where AI uses it

Everything is a vector: a token's embedding, a layer's output, a row of weights, the gradient, an image patch, a whole batch's loss values.

## 🎯 Your quest

1. `dim(v)`: its dimension.
2. `entry(v, i)`: `vᵢ` with **math counting** (i = 1 is the first entry).
3. `flat_vector(flat)`: `flat` is a dict with keys `"size"`, `"rooms"` and `"floor"`; return the vector `(size, rooms, floor)` in that order.

**Remember:** math counts from 1, Python from 0: `vᵢ` is `v[i - 1]`.

## Review

<details><summary>Say softmax(z)ᵢ = e^(zᵢ) / Σⱼ e^(zⱼ) out loud.</summary>Item i of softmax is e to the z i, divided by the sum over all j of e to the z j.</details>
<details><summary>What does θ usually stand for?</summary>All the model's parameters.</details>
