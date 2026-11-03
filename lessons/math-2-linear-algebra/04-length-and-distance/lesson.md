---
title: Length, normalizing and distance
xp: 40
---
# How long is an arrow?

> **Warm-up:** you walk 3 steps east and 4 steps north. How far are you from the start, in a straight line?

**In one sentence:** a vector's length (norm) is the square root of the sum of its squared entries: Pythagoras in any number of dimensions.

## 🔣 New symbols

| Symbol | Say it | Means | In Python |
|---|---|---|---|
| `‖v‖` | "the norm of v" / "the length of v" | `√(v₁² + v₂² + … + vₙ²)` | `math.sqrt(dot(v, v))` |
| `‖v‖₂` | "the L2 norm" | the same (the usual length) | |
| `‖v‖₁` | "the L1 norm" | `|v₁| + |v₂| + …`: "city-block" length | `sum(abs(x) for x in v)` |
| `v̂` or `v / ‖v‖` | "v hat" / "v normalized" | the **unit vector**: same direction, length 1 | `scale(1 / norm(v), v)` |
| `‖a − b‖` | "the distance between a and b" | length of the arrow from b to a | `norm(sub(a, b))` |

Double bars `‖ ‖` are for vectors; single bars `| |` (absolute value) for numbers.

## The idea

- Pythagoras: `‖(3, 4)‖ = √(9 + 16) = √25 = 5`. It works the same in 4096 dimensions: square, add, root.
- Note `‖v‖² = v · v`: the dot product of a vector with itself is its squared length.
- **Normalizing** divides by the length so every vector has length 1. Then only direction matters.
- **Distance** between two points = length of their difference. The L2 version is the "Euclidean distance".

## 🗣️ Say it out loud

`‖a − b‖₂` → "the L2 norm of a minus b" → "the straight-line distance between a and b".

## 🧮 Worked example

Normalize `(3, 4)`:

1. Length: 5
2. Divide each entry: `(3/5, 4/5) = (0.6, 0.8)`
3. Check: `√(0.36 + 0.64) = √1 = 1` ✓

## 🤖 Where AI uses it

RMSNorm and LayerNorm (LLMs 8) rescale vectors; gradient clipping caps `‖∇L‖` at 1.0; weight decay penalizes `‖θ‖²`; embedding search often normalizes vectors first; k-means uses distances.

## 🎯 Your quest

1. `norm(v)` (L2).
2. `normalize(v)`: the unit vector. Raise `ValueError` for the zero vector (it has no direction).
3. `distance(a, b)`: `‖a − b‖`.
4. `clip(g, max_norm)`: if `‖g‖ > max_norm`, return `g` scaled down to length `max_norm`; else `g` unchanged. (That's gradient clipping.)

**Remember:** length = √(sum of squares). Normalize = divide by the length.

## Review

<details><summary>Compute (1, 2, 3) · (4, 5, 6).</summary>4 + 10 + 18 = 32.</details>
<details><summary>What does a dot product of 0 mean?</summary>The vectors are perpendicular.</details>
