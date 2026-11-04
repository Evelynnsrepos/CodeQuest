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


<svg viewBox="0 0 360 230" width="100%" style="max-width:360px" role="img" aria-label="The vector (3, 2) drawn as an arrow from the origin: 3 right, 2 up"><defs><marker id="ahd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker><marker id="ah30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ah6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahe5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker></defs><line x1="30" y1="172.6" x2="332" y2="172.6" stroke="currentColor" opacity=".45"/><line x1="64.8" y1="28" x2="64.8" y2="200" stroke="currentColor" opacity=".45"/><text x="122.4" y="188.6" font-size="11" fill="currentColor" text-anchor="middle">1</text><text x="180.0" y="188.6" font-size="11" fill="currentColor" text-anchor="middle">2</text><text x="237.6" y="188.6" font-size="11" fill="currentColor" text-anchor="middle">3</text><text x="295.2" y="188.6" font-size="11" fill="currentColor" text-anchor="middle">4</text><text x="58.8" y="133.9" font-size="11" fill="currentColor" text-anchor="end">1</text><text x="58.8" y="91.2" font-size="11" fill="currentColor" text-anchor="end">2</text><text x="58.8" y="48.5" font-size="11" fill="currentColor" text-anchor="end">3</text><text x="336.0" y="176.6" font-size="12" fill="currentColor" text-anchor="start">x</text><text x="70.8" y="24.0" font-size="12" fill="currentColor" text-anchor="start">y</text><line x1="64.8" y1="172.6" x2="237.6" y2="172.6" stroke="#e5484d" stroke-width="1.5" stroke-dasharray="4 4" stroke-linecap="round"/><line x1="237.6" y1="172.6" x2="237.6" y2="87.2" stroke="#30a46c" stroke-width="1.5" stroke-dasharray="4 4" stroke-linecap="round"/><line x1="64.8" y1="172.6" x2="237.6" y2="87.2" stroke="#6c4cf5" stroke-width="3" marker-end="url(#ah6c4cf5)" stroke-linecap="round"/><text x="151.2" y="167.5" font-size="13" fill="#e5484d" text-anchor="middle">3 right</text><text x="243.4" y="129.9" font-size="13" fill="#30a46c" text-anchor="start">2 up</text><text x="139.7" y="119.3" font-size="13" fill="#6c4cf5" text-anchor="middle">(3, 2)</text></svg>

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
