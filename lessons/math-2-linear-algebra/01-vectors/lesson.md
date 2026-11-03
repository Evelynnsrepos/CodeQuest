---
title: Vectors: lists of numbers with meaning
xp: 30
---
# A vector is a list with a direction

> **Warm-up:** describe a flat with three numbers. Which three would you pick?

**In one sentence:** a vector is an ordered list of numbers, and you can picture it as an arrow.

## 🪜 Plain words

A flat could be "size, rooms, floor". Writing those three numbers in a fixed order gives a **vector**. The order matters: if you swap size and rooms, it describes a different flat.

You can also picture a vector as an **arrow**: "3 steps right, 2 steps up" is the vector (3, 2). With 3 numbers it's an arrow in 3D space. With 4096 numbers you can't picture it, but the math works exactly the same.

## 🪜 With numbers

- A flat: (65, 3, 2) → 65 m², 3 rooms, 2nd floor.
- An arrow: (3, 2) → 3 right, 2 up.
- How many numbers? That's the **dimension**: (65, 3, 2) has dimension 3.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| **v** (bold) or `v⃗` | "vector v" | a list of numbers (bold = "this is a list, not one number") | `v = [65, 3, 2]` |
| `vᵢ` | "v i" / "v sub i" | entry number i, **counting from 1** | `v[i - 1]` |
| `ℝ` | "the reals" | all ordinary numbers | `float` |
| `ℝⁿ` | "R n" | all lists of n numbers | |
| `∈` | "is in" | belongs to | |
| scalar | | a single number (not a list) | `3.5` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">v</span> <span class="k2">∈</span> <span class="k3">ℝ</span><sup><span class="k4">3</span></sup>, &nbsp; <span class="k1">v</span><sub><span class="k5">2</span></sub> = 3</div>

| Piece | Say it | Means | Flat (65, 3, 2) |
|---|---|---|---|
| <span class="k1">v</span> | "v" | the vector's name | the flat |
| <span class="k2">∈</span> | "is in" | belongs to | |
| <span class="k3">ℝ</span> | "the reals" | made of ordinary numbers | |
| <sup><span class="k4">3</span></sup> | "to the three" (here: "of length 3") | how many numbers. Here the small 3 is **not** a power, it means "lists of 3" | 3 numbers |
| <span class="k1">v</span><sub><span class="k5">2</span></sub> | "v two" | entry number 2 (math counts from 1) | rooms = 3 = `v[1]` in Python |

## 🔀 What if it were different?

<div class="wrong"><b>v₂ read as v[2]</b> (Python counting): you'd get the floor (2) instead of the rooms (3). Off-by-one is the most common bug when turning papers into code.</div>
<div class="wrong"><b>(3, 65, 2)</b> (order changed): a 3 m² flat with 65 rooms. Same numbers, different meaning.</div>
<div class="right"><b>v = (65, 3, 2), v₂ = 3</b> ✓</div>

## 🗣️ Say it out loud

`x ∈ ℝ⁴⁰⁹⁶` → "x is in R four thousand ninety-six" → "x is a list of 4096 numbers": one token's vector in Llama 3 8B.

## 🤖 Where AI uses it

Everything is a vector: a token's embedding, a layer's output, the gradient, an image patch.

## 🎯 Your quest

1. `dim(v)`: its dimension.
2. `entry(v, i)`: `vᵢ` with **math counting** (i = 1 is the first).
3. `flat_vector(flat)`: `flat` is a dict with keys `"size"`, `"rooms"`, `"floor"`; return `[size, rooms, floor]`.

**Remember:** math counts from 1, Python from 0: `vᵢ` is `v[i - 1]`.

## Review

<details><summary>Say softmax(z)ᵢ out loud.</summary>Item i of softmax of z.</details>
<details><summary>What does θ usually mean?</summary>All the model's weights.</details>
