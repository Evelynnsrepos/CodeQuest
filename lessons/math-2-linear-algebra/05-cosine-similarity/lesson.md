---
title: Angles and cosine similarity
xp: 45
---
# Same direction, whatever the length

> **Warm-up:** "cat" and "kitten" should count as similar, even if one vector is much longer. How could you compare only the **direction**?

**In one sentence:** cosine similarity is the dot product divided by both lengths, giving a number from −1 (opposite) to 1 (same direction).

## 🪜 Plain words

The dot product mixes two things: how much the arrows point the same way **and** how long they are. To keep only the direction, divide the length back out. What's left is a score:

- 1 → exactly the same direction
- 0 → at a right angle, unrelated
- −1 → exactly opposite

That score is called the **cosine** of the angle between them.

## 🪜 With numbers

(1, 0) and (1, 1): dot = 1. Lengths 1 and about 1.414. 1 divided by (1 times 1.414) ≈ **0.707**: fairly similar (the angle is 45°).

(2, 0) and (5, 0): dot 10, lengths 2 and 5, 10 / 10 = **1**: same direction, even though one is longer.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `θ` | "theta" | here: the **angle** between two arrows | |
| `cos θ` | "cosine theta" | 1 at 0°, 0 at 90°, −1 at 180° | `math.cos` (radians!) |
| `cos⁻¹` / `arccos` | "arc cosine" | the angle for a cosine value (the ⁻¹ means "reverse function", not 1/cos) | `math.acos` |
| `‖a‖` | "the length of a" | | |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">cos θ</span> = <span class="k2">a · b</span> / ( <span class="k3">‖a‖</span> · <span class="k4">‖b‖</span> )</div>

| Piece | Say it | Means | (1, 0) and (1, 1) |
|---|---|---|---|
| <span class="k1">cos θ</span> | "cosine theta" | the similarity score | 0.707 |
| <span class="k2">a · b</span> | "a dot b" | how much they agree, including length | 1 |
| `/` ( … ) | "divided by" | divide by the whole bottom | |
| <span class="k3">‖a‖</span> | "length of a" | | 1 |
| <span class="k4">‖b‖</span> | "length of b" | | 1.414 |

## 🔀 What if it were different?

<div class="wrong"><b>a · b alone</b>: compare query (1, 0) with "short match" (1, 0.1) and "long but off" (10, 10): dot products 1 and 10. The long one wins although it points 45° away.</div>
<div class="wrong"><b>a · b / ‖a‖</b> (only one length): the long vector still wins (10 vs 1). Both lengths must go.</div>
<div class="right"><b>a · b / (‖a‖ ‖b‖)</b>: 0.995 vs 0.707 → the short, well-aligned one wins ✓</div>

## 🗣️ Say it out loud

"cos theta equals a dot b, divided by the length of a times the length of b."

## 🤖 Where AI uses it

Semantic search and RAG, CLIP, deduplication, comparing embeddings.

## 🎯 Your quest

1. `cosine(a, b)`
2. `angle_degrees(a, b)`: clamp the cosine into [−1, 1] before `math.acos`, then `math.degrees`.
3. `most_similar(query, items)`: `items` is name → vector; the name with the highest cosine.

**Remember:** cosine similarity only cares about direction.

## Review

<details><summary>‖(6, 8)‖ = ?</summary>10.</details>
<details><summary>What does gradient clipping do?</summary>Shrinks the gradient to a maximum length if it's too long.</details>
