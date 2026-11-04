---
title: Spawning around the player
xp: 25
---
# Enemies from every side

Survival shooters spawn enemies **around** the player, just off screen, so they don't pop up right on top of you. That means picking points on a **circle**.

You already know the trick from the bullets lesson: `Vector2.from_angle(angle)` is a length-1 arrow pointing at that angle. Make it `radius` long and add it to the centre:

```
point = center + Vector2.from_angle(angle) * radius
```

Example: center `(0, 0)`, radius `100`, angle `PI / 2` (down): `(0, 1) × 100 = (0, 100)`.

## Evenly spaced

For `count` enemies spread evenly, split the full turn `TAU` into `count` equal slices. Enemy `i` gets the angle `TAU / count * i`. With 4 enemies:

```
TAU / 4 = a quarter turn (90°)
i = 0 → 0°      right
i = 1 → 90°     down
i = 2 → 180°    left
i = 3 → 270°    up
```

## Random

For a random direction, pick a random angle: `randf()` gives a random number from `0` to `1`, so `randf() * TAU` is a random angle anywhere around the circle.

## Your quest

1. `ring_points(center: Vector2, radius: float, count: int) -> Array` returns `count` evenly spaced points on the circle, starting at angle `0`.
2. `random_point(center: Vector2, radius: float) -> Vector2` returns one random point on the circle.
