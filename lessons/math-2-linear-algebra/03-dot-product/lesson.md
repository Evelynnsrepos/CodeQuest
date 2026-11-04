---
title: The dot product
xp: 45
---
# One number that says "how much do these agree?"

> **Warm-up:** a shop gives 2 points per apple, 5 per melon, 1 per lemon. You buy 3 apples, 1 melon, 4 lemons. How many points?

**In one sentence:** the dot product multiplies two lists position by position and adds everything up, giving one number.

## 🪜 Plain words

Points per item times how many of each, then add it all up. That's it. Two lists go in, **one number** comes out.

If you picture the two lists as arrows, that number also says how much they **point the same way**: big and positive = same way, zero = at a right angle (unrelated), negative = opposite ways.

## 🪜 With numbers

Points: (2, 5, 1). Basket: (3, 1, 4). 2 times 3 = 6, 5 times 1 = 5, 1 times 4 = 4. Total **15**.

Arrows (1, 2) and (2, −1): 1 times 2 + 2 times (−1) = 2 − 2 = **0** → at a right angle.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| **a** · **b** | "a dot b" | multiply position by position, add up | `sum(x * y for x, y in zip(a, b))` |
| `Σᵢ aᵢbᵢ` | "the sum over i of a i b i" | the same, written as a sum | |
| **a**ᵀ**b** | "a transpose b" | the same again, matrix style (lesson 9) | |
| `⟨a, b⟩` | "the inner product of a and b" | the same again | |
| `⊥` | "is perpendicular to" | dot product is 0 | |

Four ways to write the same thing: papers use all of them.

## 🔬 Take the formula apart

<div class="formula"><span class="k1">a · b</span> = <span class="k2">Σ</span><sub><span class="k3">i</span></sub> <span class="k4">aᵢ</span> <span class="k5">bᵢ</span></div>

| Piece | Say it | Means | Points (2,5,1) · basket (3,1,4) |
|---|---|---|---|
| <span class="k1">a · b</span> | "a dot b" | the answer: one number | 15 |
| <span class="k2">Σ</span> | "the sum of" | add up… | |
| <sub><span class="k3">i</span></sub> | "over i" | …for every position i | i = 1, 2, 3 |
| <span class="k4">aᵢ</span> | "a i" | entry i of a | 2, 5, 1 |
| <span class="k5">bᵢ</span> | "b i" | entry i of b, **times** aᵢ (invisible times) | 3, 1, 4 → 6, 5, 4 |

## 🔀 What if it were different?

<div class="wrong"><b>(Σ aᵢ) · (Σ bᵢ)</b> (add first, multiply after): 8 · 8 = 64 points. That gives melon points for lemons!</div>
<div class="wrong"><b>Σ (aᵢ + bᵢ)</b>: 5 + 6 + 5 = 16. Adding points to item counts makes no sense.</div>
<div class="wrong"><b>Different lengths</b> (3 prices, 2 items): undefined. Python's zip would silently drop the last one, a sneaky bug.</div>
<div class="right"><b>Σ aᵢbᵢ</b> = 6 + 5 + 4 = 15 ✓</div>

## 🗣️ Say it out loud

`q · k / √d` → "q dot k over root d" → "how well this query matches that key" (attention).

## 🤖 Where AI uses it

A neuron (`w · x + b`), attention scores (`q · k`), search by meaning (RAG), and every matrix product is many dot products.

## 🎯 Your quest

1. `dot(a, b)`; raise `ValueError` if the lengths differ.
2. `neuron(w, x, b)`: `w · x + b`.
3. `relation(a, b)`: `"same direction"`, `"perpendicular"` or `"opposite"` from the sign of the dot product.

**Remember:** multiply pairs, then add. Positive = agree.

## Review

<details><summary>2·(1, −3) = ?</summary>(2, −6).</details>
<details><summary>What does [1, 2] + [3, 4] give in plain Python?</summary>[1, 2, 3, 4].</details>
