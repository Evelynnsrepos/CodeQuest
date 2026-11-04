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

<svg viewBox="0 0 400 245" width="100%" style="max-width:400px" role="img" aria-label="The player turns to the target by the angle of the arrow from the player to the target, measured from pointing right"><defs><marker id="aham6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahame5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker><marker id="aham30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ahamd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker></defs><line x1="90.0" y1="70.0" x2="380.0" y2="70.0" stroke="currentColor" stroke-width="1" stroke-dasharray="5 4" opacity="0.6"/><text x="380.0" y="62.0" font-size="11" fill="currentColor" text-anchor="end">angle 0 = right</text><line x1="90.0" y1="70.0" x2="285.0" y2="187.0" stroke="#6c4cf5" stroke-width="2.5" marker-end="url(#aham6c4cf5)"/><circle cx="290.0" cy="190.0" r="6" fill="#e5484d"/><text x="300.0" y="194.0" font-size="12" fill="#e5484d" text-anchor="start">target</text><circle cx="90.0" cy="70.0" r="8" fill="#6c4cf5"/><text x="90.0" y="56.0" font-size="12" fill="#6c4cf5" text-anchor="middle">player</text><path d="M150,70 A60,60 0 0,1 141.4,100.9" stroke="#d97706" stroke-width="2" fill="none"/><text x="162.0" y="104.0" font-size="11" fill="#d97706" text-anchor="start">31° (about 0.54 radians)</text><text x="215.0" y="120.0" font-size="12" fill="#6c4cf5" text-anchor="start" font-weight="bold">(target − position).angle()</text><text x="20.0" y="230.0" font-size="11" fill="currentColor" text-anchor="start">y points down in 2D, so a positive angle turns clockwise</text></svg>

## Your quest

Write `aim_at(target: Vector2)` that sets `rotation` so the player faces `target`, without using `look_at` (so you see what it does).

## Review

<details><summary>What does Vector2.angle() return?</summary>The angle of the arrow in radians, measured from pointing right.</details>
<details><summary>What is a radian?</summary>A unit for angles: a full turn is TAU (about 6.28) radians, half a turn is PI.</details>
