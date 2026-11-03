---
title: Angles and cosine similarity
xp: 45
---
# Same direction, whatever the length

> **Warm-up:** "cat" and "kitten" should be similar; "cat" and "tax return" not. If both are vectors, how could you measure "pointing the same way" without caring how long they are?

**In one sentence:** cosine similarity is the dot product of the two normalized vectors, a number from −1 (opposite) to 1 (same direction).

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `θ` | "theta" | here: the **angle** between two vectors | |
| `cos θ` | "cosine theta" | from 1 (0°) through 0 (90°) to −1 (180°) | `math.cos(theta)` (radians!) |
| `cos(a, b)` | "the cosine similarity of a and b" | `(a · b) / (‖a‖ · ‖b‖)` | |
| `arccos` or `cos⁻¹` | "arc cosine" | the angle whose cosine is a value | `math.acos(x)` |
| `°` / rad | degrees / radians | 180° = π radians | `math.degrees(r)` |

`cos⁻¹` means the **inverse function**, not `1/cos`. Confusing, but standard.

## The idea

There's a geometric formula for the dot product:

```
a · b = ‖a‖ · ‖b‖ · cos θ
```

Solve it for `cos θ`:

```
cos θ = (a · b) / (‖a‖ · ‖b‖)
```

Dividing by both lengths removes the effect of size, leaving only the direction. Read the result as:

| cos θ | angle | meaning |
|---|---|---|
| 1 | 0° | same direction |
| ~0.7 | 45° | related |
| 0 | 90° | unrelated |
| −1 | 180° | opposite |

## 🗣️ Say it out loud

`cos(a, b) = a·b / (‖a‖‖b‖)` → "a dot b, divided by the length of a times the length of b".

## 🧮 Worked example

`a = (1, 0)`, `b = (1, 1)`:

1. `a · b = 1`
2. `‖a‖ = 1`, `‖b‖ = √2 ≈ 1.414`
3. `cos θ = 1 / 1.414 ≈ 0.707`
4. `θ = arccos(0.707) = 45°`

## 🤖 Where AI uses it

Semantic search and RAG (LLMs 3), CLIP's zero-shot classification, deduplication by embedding, comparing what layers of a model represent.

## 🎯 Your quest

`dot` and `norm` are given.

1. `cosine(a, b)`
2. `angle_degrees(a, b)`: the angle in degrees (clamp the cosine into `[−1, 1]` before `math.acos`, because rounding can give 1.0000000002).
3. `most_similar(query, items)`: `items` is a dict name → vector; return the name with the highest cosine similarity.

**Remember:** cosine similarity only cares about direction.

## Review

<details><summary>‖(6, 8)‖ = ?</summary>10.</details>
<details><summary>What does gradient clipping do?</summary>If the gradient is longer than a maximum, scales it down to that length.</details>
