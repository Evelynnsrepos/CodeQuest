---
title: Spawning around the player
xp: 25
hint: The angle for point i is TAU / count * i.
hint: center + Vector2.from_angle(angle) * radius gives a point on the circle. For random_point use randf() * TAU as the angle.
---
# Enemies from every side

> **Warm-up:** Why do enemies in survival shooters appear around the edges, not on top of you?

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

<svg viewBox="0 0 340 280" width="100%" style="max-width:340px" role="img" aria-label="Eight spawn points evenly spaced on a circle around the player, an eighth of a turn apart"><defs><marker id="ahsr6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahsre5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker><marker id="ahsr30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ahsrd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker></defs><circle cx="170" cy="135" r="95" stroke="currentColor" fill="none" opacity=".4" stroke-dasharray="5 4"/><rect x="161.0" y="126.0" width="18.0" height="18.0" fill="#6c4cf5" rx="2"/><text x="170.0" y="163.0" font-size="11" fill="#6c4cf5" text-anchor="middle">player</text><line x1="170.0" y1="135.0" x2="259.0" y2="135.0" stroke="#d97706" stroke-width="1.5" marker-end="url(#ahsrd97706)"/><text x="217.5" y="129.0" font-size="11" fill="#d97706" text-anchor="middle">radius</text><circle cx="265.0" cy="135.0" r="6" fill="#e5484d"/><text x="287.0" y="139.0" font-size="11" fill="#e5484d" text-anchor="middle">i=0</text><circle cx="237.2" cy="202.2" r="6" fill="#e5484d"/><text x="252.7" y="221.7" font-size="11" fill="#e5484d" text-anchor="middle">i=1</text><circle cx="170.0" cy="230.0" r="6" fill="#e5484d"/><text x="170.0" y="256.0" font-size="11" fill="#e5484d" text-anchor="middle">i=2</text><circle cx="102.8" cy="202.2" r="6" fill="#e5484d"/><text x="87.3" y="221.7" font-size="11" fill="#e5484d" text-anchor="middle">i=3</text><circle cx="75.0" cy="135.0" r="6" fill="#e5484d"/><text x="53.0" y="139.0" font-size="11" fill="#e5484d" text-anchor="middle">i=4</text><circle cx="102.8" cy="67.8" r="6" fill="#e5484d"/><text x="87.3" y="56.3" font-size="11" fill="#e5484d" text-anchor="middle">i=5</text><circle cx="170.0" cy="40.0" r="6" fill="#e5484d"/><text x="170.0" y="22.0" font-size="11" fill="#e5484d" text-anchor="middle">i=6</text><circle cx="237.2" cy="67.8" r="6" fill="#e5484d"/><text x="252.7" y="56.3" font-size="11" fill="#e5484d" text-anchor="middle">i=7</text><text x="170.0" y="268.0" font-size="11" fill="currentColor" text-anchor="middle">angle for point i = TAU / 8 × i (an eighth of a turn each)</text></svg>

## Your quest

1. `ring_points(center: Vector2, radius: float, count: int) -> Array` returns `count` evenly spaced points on the circle, starting at angle `0`.
2. `random_point(center: Vector2, radius: float) -> Vector2` returns one random point on the circle.

## Review

<details><summary>What is TAU?</summary>One full turn in radians, about 6.28 (2 x PI).</details>
<details><summary>How do you get a point on a circle?</summary>center + Vector2.from_angle(angle) * radius</details>
