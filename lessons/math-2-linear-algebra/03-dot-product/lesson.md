---
title: The dot product
xp: 45
---
# One number that says "how much do these agree?"

> **Warm-up:** a shop gives points: 2 per apple, 5 per melon, 1 per lemon. You buy 3 apples, 1 melon, 4 lemons. How many points? You just did a dot product.

**In one sentence:** the dot product multiplies two vectors entry by entry and adds up the results, giving one number.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `a · b` | "a dot b" | `a₁b₁ + a₂b₂ + … + aₙbₙ` | `sum(x * y for x, y in zip(a, b))` |
| `Σᵢ aᵢbᵢ` | "sum over i of a i b i" | the same, as a sum (Math 1, lesson 8) | |
| `aᵀb` | "a transpose b" | the same again, in matrix notation (lesson 9) | |
| `⟨a, b⟩` | "the inner product of a and b" | yet another way to write it | |
| `a ⊥ b` | "a is perpendicular to b" | `a · b = 0` | |

Four notations, one idea. Papers use all of them.

## The idea

`(2, 5, 1) · (3, 1, 4) = 2·3 + 5·1 + 1·4 = 6 + 5 + 4 = 15`.

What the sign tells you (for arrows):

- **positive**: they point roughly the same way
- **zero**: at a right angle (perpendicular / **orthogonal**): "unrelated"
- **negative**: roughly opposite

The size also grows with the vectors' lengths (lesson 4 fixes that with cosine).

Another view: `w · x` is a **weighted sum** of x's entries with weights w. That's exactly a neuron.

## 🗣️ Say it out loud

`score = q · k / √d` → "the score is q dot k, divided by root d" → "how well does this query match that key?" (attention).

## 🧮 Worked example

`(1, 2) · (2, −1) = 1·2 + 2·(−1) = 2 − 2 = 0` → perpendicular.

`(1, 2) · (3, 4) = 3 + 8 = 11` → same general direction.

## 🤖 Where AI uses it

A neuron (`w · x + b`), attention scores (`q · k`), similarity search in RAG (dot product of embeddings), and every matrix multiplication is many dot products (lesson 7).

## 🎯 Your quest

1. `dot(a, b)`; raise `ValueError` if the lengths differ (math says it's undefined).
2. `neuron(w, x, b)`: `w · x + b`.
3. `relation(a, b)`: `"same direction"`, `"perpendicular"` or `"opposite"` from the sign of the dot product.

**Remember:** dot product = multiply pairs, then add. Positive means "agree".

## Review

<details><summary>What is 2·(1, −3)?</summary>(2, −6).</details>
<details><summary>What does [1, 2] + [3, 4] give in plain Python?</summary>[1, 2, 3, 4]: lists are glued, not added.</details>
