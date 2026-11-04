---
title: Projections: the shadow of a vector
xp: 55
---
# How much of a points along b?

> **Warm-up:** the sun is straight overhead. A stick leans at an angle. How long is its shadow on the ground?

**In one sentence:** the projection of a onto b is the part of a that points in b's direction: its "shadow" on the line through b.

## 🪜 Plain words

Any arrow a can be split into two pieces: one **along** b (the shadow) and one **at a right angle** to b (what's left). The shadow is a stretched copy of b. How much to stretch it? The dot product a · b (Math 2 lesson 03) measures how much a and b agree; divide by b · b so b's own length doesn't count twice.

The leftover piece is **perpendicular** to b: its dot product with b is 0. That's what makes the shadow the **closest point** on b's line to a.

## 🪜 With numbers

a = (3, 4), b = (2, 0) (along the floor).

- a · b = 3·2 + 4·0 = 6; b · b = 2·2 + 0·0 = 4.
- stretch = 6 / 4 = 1.5; shadow = 1.5 · (2, 0) = **(3, 0)**.
- leftover = a − shadow = (0, 4). Check: (0, 4) · (2, 0) = 0 ✓ perpendicular.

<svg viewBox="0 0 300 200" width="100%" style="max-width:300px" role="img" aria-label="Vector a from the origin to (3,4), its shadow (3,0) along b, and the dashed leftover (0,4) at a right angle">
  <g transform="translate(30,170) scale(1,-1)" fill="none" stroke-linecap="round">
    <line x1="0" y1="0" x2="240" y2="0" stroke="currentColor" opacity=".25"/>
    <line x1="0" y1="0" x2="120" y2="0" stroke="#e5484d" stroke-width="4"/>
    <line x1="0" y1="0" x2="80" y2="0" stroke="#30a46c" stroke-width="2"/>
    <line x1="0" y1="0" x2="120" y2="160" stroke="#6c4cf5" stroke-width="3"/>
    <line x1="120" y1="0" x2="120" y2="160" stroke="currentColor" stroke-dasharray="5 5"/>
  </g>
  <g font-size="13" fill="currentColor">
    <text x="20" y="95">a = (3, 4)</text><text x="75" y="192" fill="#e5484d">shadow (3, 0)</text>
    <text x="62" y="160" fill="#30a46c">b = (2, 0)</text><text x="155" y="100">leftover (0, 4)</text>
  </g>
</svg>

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `a · b` | "a dot b" | multiply matching numbers, add | `sum(x*y for x, y in zip(a, b))` |
| `proj_b(a)` | "projection of a onto b" | the shadow | |
| `⊥` | "perpendicular" | at a right angle; dot product 0 | `dot(u, v) == 0` |
| `‖b‖` | "norm of b" | length | `math.sqrt(dot(b, b))` |

## 🔬 Take the formula apart

<div class="formula"><span class="k1">proj_b(a)</span> = ( <span class="k2">a · b</span> / <span class="k3">b · b</span> ) <span class="k4">b</span></div>

| Piece | Say it | Means | Example |
|---|---|---|---|
| <span class="k2">a · b</span> | "a dot b" | how much a and b agree | 6 |
| <span class="k3">b · b</span> | "b dot b" | b's length squared, to cancel it | 4 |
| ( … / … ) | "over" | the stretch factor | 1.5 |
| <span class="k4">b</span> | "b" | the direction we stretch | (2, 0) |
| <span class="k1">proj_b(a)</span> | "projection" | the shadow | (3, 0) |

## 🔀 What if it were different?

<div class="wrong"><b>Divide by ‖b‖ instead of b · b</b>: 6 / 2 = 3, shadow = (6, 0). Twice too long, because b's length is counted once in a · b and once more in the vector b itself.</div>
<div class="wrong"><b>Forget to multiply by b</b>: you get the number 1.5, a length in units of b, not the shadow vector.</div>
<div class="right">(6 / 4) · (2, 0) = (3, 0); leftover (0, 4) ⊥ b ✓</div>

## 🗣️ Say it out loud

"The projection of a onto b is a dot b over b dot b, times b."

## 🤖 Where AI uses it

Least-squares regression is a projection: the predictions are the shadow of the targets on the space your features can reach. PCA (lesson 04) projects data onto its main directions. In embedding work, you can **remove** a direction (e.g. a bias direction) by subtracting the projection onto it.

## 🎯 Your quest

1. `project(a, b)`: the projection vector.
2. `reject(a, b)`: the leftover, `a − project(a, b)`.
3. `remove_direction(vectors, d)`: return each vector with its projection onto `d` removed.

**Remember:** stretch b by (a·b)/(b·b); the leftover is perpendicular.

## Review

<details><summary>Does r = 0 mean two things are unrelated?</summary>No; r only measures straight-line relationships. y = x² can give r = 0.</details>
