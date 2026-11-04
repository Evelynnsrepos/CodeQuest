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


<svg viewBox="0 0 360 230" width="100%" style="max-width:360px" role="img" aria-label="Arrows (1, 0) and (1, 1) with a 45 degree angle between them: cosine 0.707"><defs><marker id="ahd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker><marker id="ah30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ah6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahe5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker></defs><line x1="30" y1="169.1" x2="332" y2="169.1" stroke="currentColor" opacity=".45"/><line x1="69.2" y1="28" x2="69.2" y2="200" stroke="currentColor" opacity=".45"/><text x="180.0" y="185.1" font-size="11" fill="currentColor" text-anchor="middle">1</text><text x="290.8" y="185.1" font-size="11" fill="currentColor" text-anchor="middle">2</text><text x="63.2" y="89.9" font-size="11" fill="currentColor" text-anchor="end">1</text><text x="336.0" y="173.1" font-size="12" fill="currentColor" text-anchor="start">x</text><text x="75.2" y="24.0" font-size="12" fill="currentColor" text-anchor="start">y</text><line x1="69.2" y1="169.1" x2="180.0" y2="169.1" stroke="#6c4cf5" stroke-width="3" marker-end="url(#ah6c4cf5)" stroke-linecap="round"/><line x1="69.2" y1="169.1" x2="180.0" y2="85.9" stroke="#e5484d" stroke-width="3" marker-end="url(#ahe5484d)" stroke-linecap="round"/><polyline points="108.0,169.1 108.0,167.9 107.9,166.8 107.7,165.6 107.5,164.5 107.3,163.4 106.9,162.3 106.5,161.2 106.1,160.1 105.6,159.0 105.0,157.9 104.4,156.9 103.8,155.8 103.1,154.8 102.3,153.8 101.5,152.9 100.6,151.9 99.7,151.0 98.7,150.2 97.7,149.3 96.6,148.5" fill="none" stroke="#d97706" stroke-width="2"/><text x="119.1" y="159.1" font-size="13" fill="#d97706" text-anchor="start">45°</text><text x="188.9" y="162.4" font-size="13" fill="#6c4cf5" text-anchor="start">(1, 0)</text><text x="185.5" y="81.7" font-size="13" fill="#e5484d" text-anchor="start">(1, 1)</text><text x="246.5" y="127.5" font-size="13" fill="#d97706" text-anchor="middle">cos 45° ≈ 0.707</text></svg>

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
