---
title: Aiming with angles
xp: 25
hint: The arrow from you to the target is target - global_position.
hint: rotation = (target - global_position).angle()
---
# Look at the mouse

> **Warm-up:** In a top-down shooter, how does the game know which way to turn your character?

In a top-down shooter the player turns to face the mouse. A node's `rotation` is an **angle**, so let's look at how Godot measures angles.

## Radians

Godot measures angles in **radians**, not degrees. A full turn is 360°, which is `2π` radians (π, "pi", is about `3.14159`). Godot calls a full turn `TAU` (`2π` ≈ `6.283`).

| degrees | radians | Godot |
| --- | --- | --- |
| 0° | 0 | `0` |
| 90° | π/2 ≈ 1.571 | `PI / 2` |
| 180° | π ≈ 3.142 | `PI` |
| 360° | 2π ≈ 6.283 | `TAU` |

To convert: `deg_to_rad(90)` gives `1.571` and `rad_to_deg(PI)` gives `180`.

## Which way is 0?

Angle `0` points **right** (along +x). Because y points **down** in 2D, a positive angle turns **clockwise** on screen: `PI / 2` points straight **down**, and `-PI / 2` points **up**.

## The angle of an arrow

To face a target:

1. Make the arrow from you to the target: `target - global_position` (the subtraction from the vector math lesson).
2. Ask the arrow for its angle: `.angle()`.

```
you at (0, 0), mouse at (0, 50)
arrow = (0, 50) - (0, 0) = (0, 50)    → straight down
(0, 50).angle() = PI / 2              → 90°, pointing down ✔
```

Under the hood `.angle()` uses a trigonometry function called **atan2(y, x)**, which works out the angle from the two sides of the triangle. You don't need to compute it by hand, just know that's what it's for.

In a game you'd get the mouse with `get_global_mouse_position()`. Godot also has a shortcut, `look_at(target)`, that does both steps in one go.

## Your quest

Write `aim_at(target: Vector2)` that sets `rotation` so the player faces `target`, without using `look_at` (so you see what it does).

## Review

<details><summary>What does Vector2.angle() return?</summary>The angle of the arrow in radians, measured from pointing right.</details>
<details><summary>What is a radian?</summary>A unit for angles: a full turn is TAU (about 6.28) radians, half a turn is PI.</details>
