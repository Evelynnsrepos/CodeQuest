---
title: Running with acceleration
xp: 25
hint: var direction := Input.get_axis("ui_left", "ui_right")
hint: velocity.x = move_toward(velocity.x, direction * max_speed, acceleration * delta), and the same towards 0 with friction when direction is 0.
---
# Speeding up and slowing down

> **Warm-up:** Why does a character that starts and stops instantly feel stiff?

The simplest movement sets the speed straight away: `velocity.x = direction * speed`. It works, but feels stiff, like a robot. Most platformers **accelerate** to full speed and **slow down** (friction) when you let go. It's a tiny delay, but it makes movement feel smooth.

`move_toward(from, to, step)` moves a number towards a target by at most `step`, and never past it:

```gdscript
move_toward(0, 300, 20)     # 20   (moved up by 20)
move_toward(290, 300, 20)   # 300  (would be 310, but stops at the target)
move_toward(300, 0, 50)     # 250  (moves down too)
```

So each frame we nudge the current speed towards the speed we *want*:

```gdscript
var target := direction * max_speed
velocity.x = move_toward(velocity.x, target, acceleration * delta)
```

With `acceleration = 1200` px/s², each frame adds `1200 × 1/60 = 20` px/s. To reach `max_speed = 300` that takes `300 ÷ 1200 = 0.25` s, about 15 frames.

`Input.get_axis("ui_left", "ui_right")` gives `-1` (left), `1` (right) or `0` (neither, or both).

## Your quest

The gravity code is already there. Add horizontal movement:

1. Read the direction with `Input.get_axis("ui_left", "ui_right")`.
2. If the direction isn't `0`, move `velocity.x` towards `direction * max_speed` by `acceleration * delta`.
3. Otherwise, move `velocity.x` towards `0` by `friction * delta`.

## Review

<details><summary>What does Input.get_axis("ui_left", "ui_right") give?</summary>-1 for left, 1 for right, 0 for neither (or both).</details>
<details><summary>Why use friction bigger than acceleration?</summary>Stopping a bit faster than starting feels responsive.</details>
