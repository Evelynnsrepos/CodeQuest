---
title: Bullets that fly
xp: 25
hint: Vector2.from_angle(rotation) is the direction the bullet faces, length 1.
hint: position += Vector2.from_angle(rotation) * speed * delta, then lifetime -= delta and queue_free() when lifetime <= 0.
---
# From angle back to arrow

> **Warm-up:** A bullet points at 45 degrees. How does it know how far to move right and how far down?

Last lesson turned an arrow into an angle. A bullet needs the opposite: it has a `rotation` and must fly that way. Which arrow (of length 1) points at an angle?

## Cosine and sine

Picture a circle with radius 1 around the bullet. Walk around the circle by the angle, starting from the right side. The point you reach is:

```
x = cos(angle)
y = sin(angle)
```

**cos** (cosine) and **sin** (sine) are just the names of the functions that give these two numbers. A few to get a feel for them:

| angle | cos (x) | sin (y) | arrow |
| --- | --- | --- | --- |
| 0 | 1 | 0 | → right |
| PI / 2 (90°) | 0 | 1 | ↓ down |
| PI (180°) | -1 | 0 | ← left |
| PI / 4 (45°) | 0.707 | 0.707 | ↘ diagonal |

The last row is interesting: 0.707 isn't 0.5, because the arrow must still have length 1. Check it with Pythagoras: 0.707² + 0.707² = 0.5 + 0.5 = 1 ✔.

Godot wraps this up for you: `Vector2.from_angle(rotation)` returns `Vector2(cos(rotation), sin(rotation))`.

## Moving and disappearing

So the bullet moves with:

```gdscript
position += Vector2.from_angle(rotation) * speed * delta
```

Bullets that miss would fly forever and slow the game down, so give each one a **lifetime** and remove it with `queue_free()` when it runs out.

## Your quest

Write the bullet's `_physics_process(delta)`:

1. Move along its `rotation` at `speed` pixels per second.
2. Count `lifetime` down by `delta`, and `queue_free()` the bullet when it reaches `0` or less.

## Review

<details><summary>What does Vector2.from_angle(a) give?</summary>A length-1 arrow pointing at angle a.</details>
<details><summary>Why give bullets a lifetime?</summary>So missed bullets are removed instead of flying forever and slowing the game.</details>
