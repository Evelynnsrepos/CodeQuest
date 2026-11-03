---
title: Length, normalizing and distance
xp: 40
---
# How long is an arrow?

> **Warm-up:** you walk 3 steps east and 4 north. How far are you from the start in a straight line?

**In one sentence:** a vector's length is the square root of the sum of its squared entries (Pythagoras), in any number of dimensions.

## 🪜 Plain words

The east steps and north steps form a right-angled triangle; the straight line home is its long side. The old rule (Pythagoras): square both sides, add, take the square root. With more dimensions you just square and add **more** numbers.

**Normalizing** shrinks or stretches an arrow to length exactly 1, keeping its direction. **Distance** between two points = length of the arrow from one to the other.

## 🪜 With numbers

- (3, 4): 3 times 3 = 9, 4 times 4 = 16, total 25, square root **5**.
- Normalize (3, 4): divide each by 5 → (0.6, 0.8). Check: 0.36 + 0.64 = 1, root 1 ✓.
- Distance from (1, 1) to (4, 5): difference (3, 4) → length 5.

## 🔣 The signs

| Sign | Say it | Means | In Python |
|---|---|---|---|
| `‖v‖` | "the norm of v" / "the length of v" | √(v₁² + v₂² + …) | `math.sqrt(sum(x*x for x in v))` |
| `‖v‖₂` | "the L2 norm" | the same (normal length) | |
| `‖v‖₁` | "the L1 norm" | \|v₁\| + \|v₂\| + …: walking along streets | |
| `v / ‖v‖` or `v̂` | "v normalized" / "v hat" | length-1 version | |
| `‖a − b‖` | "the distance between a and b" | | |

Double bars `‖ ‖` are for lists; single bars `| |` for one number.

## 🔬 Take the formula apart

<div class="formula"><span class="k1">‖v‖</span> = <span class="k2">√</span>( <span class="k3">Σ</span><sub>i</sub> <span class="k4">vᵢ</span><span class="k5">²</span> )</div>

| Piece | Say it | Means | v = (3, 4) |
|---|---|---|---|
| <span class="k1">‖v‖</span> | "the length of v" | the answer | 5 |
| <span class="k4">vᵢ</span> | "v i" | each entry | 3, 4 |
| <span class="k5">²</span> | "squared" | times itself (also removes minus signs) | 9, 16 |
| <span class="k3">Σ</span><sub>i</sub> | "sum over i" | add them all | 25 |
| <span class="k2">√</span>( ) | "the square root of" | undo the squaring, once, at the end | 5 |

## 🔀 What if it were different?

<div class="wrong"><b>Σ vᵢ</b> (no squares, no root): 3 + 4 = 7. And for (3, −4) it would be −1: a negative length!</div>
<div class="wrong"><b>Σ √(vᵢ²)</b> (root inside): 3 + 4 = 7. That's the L1 (street) length, a different thing.</div>
<div class="wrong"><b>Σ vᵢ²</b> (forgot the root): 25. That's the length <i>squared</i>.</div>
<div class="right"><b>√(Σ vᵢ²)</b> = 5 ✓</div>

## 🗣️ Say it out loud

`‖v‖ = √(Σᵢ vᵢ²)` → "the norm of v is the square root of the sum of the squared entries."

## 🤖 Where AI uses it

RMSNorm (LLMs 8), **gradient clipping** (if ‖gradient‖ > 1, shrink it to 1), weight decay (penalizes ‖θ‖²), normalized embeddings.

## 🎯 Your quest

1. `norm(v)`
2. `normalize(v)`: raise `ValueError` for the zero vector (no direction).
3. `distance(a, b)`: `‖a − b‖`.
4. `clip(g, max_norm)`: if `‖g‖ > max_norm`, scale g down to length max_norm; else return g.

**Remember:** length = √(sum of squares).

## Review

<details><summary>(1, 2, 3) · (4, 5, 6) = ?</summary>32.</details>
<details><summary>A dot product of 0 means…</summary>The vectors are at a right angle (unrelated).</details>
