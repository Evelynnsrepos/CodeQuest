---
title: Day and night
xp: 30
hint: Time moves by 24.0 / day_length * delta hours; fposmod(..., 24.0) wraps 24 back to 0.
hint: angle = time_of_day / 24.0 * TAU, day_amount = (1.0 - cos(angle)) / 2.0, then lerpf(night_brightness, 1.0, day_amount).
---
# The sun goes down

> **Warm-up:** How bright is it at midnight, at sunrise and at noon?

A survival day might last 10 real minutes. We keep the in-game clock as `time_of_day`, in hours from `0` to `24`, and move it forward every frame.

## Wrapping around midnight

After 23:59 comes 0:00, not 24:00. `fposmod(value, 24.0)` wraps a number into the range 0–24, like a clock:

```
fposmod(25.0, 24.0) = 1.0     (1 am the next day)
fposmod(23.5, 24.0) = 23.5    (unchanged)
fposmod(48.0, 24.0) = 0.0
```

("mod" is short for modulo: what's left over after taking away as many whole 24s as possible.)

## Hours per real second

If a full day (24 hours) lasts `day_length` real seconds, then each real second moves the clock forward by `24 / day_length` hours. With `day_length = 600` that's 0.04 hours (2.4 minutes) per second.

## Brightness that rises and falls smoothly

The light should be darkest at midnight (`0`), brightest at noon (`12`) and change gently in between. A **cosine** wave does exactly that. Let's build it in three steps.

**Step 1. Turn the hour into an angle.** One full day is one full turn: `angle = time_of_day / 24 × TAU`. Midnight is angle 0, noon is half a turn (`PI`).

**Step 2. Take the cosine.** You met cos in the shooter course: `cos(0) = 1` and `cos(PI) = -1`. In between it moves smoothly. So cos goes `1` at midnight, `-1` at noon, `1` again at the next midnight.

**Step 3. Flip and squeeze it to 0–1.** We want 0 at midnight and 1 at noon, the other way round, and without negative numbers:

```
day_amount = (1 - cos(angle)) / 2
```

Check midnight: (1 - 1) / 2 = 0 ✔. Check noon: (1 - (-1)) / 2 = 2 / 2 = 1 ✔. At 6 am, angle is a quarter turn, cos = 0, so (1 - 0) / 2 = 0.5, halfway ✔.

**Step 4. Blend.** Nights shouldn't be pitch black, so blend between `night_brightness` (0.2) and 1.0. `lerpf(a, b, t)` (*linear interpolation*) gives `a` when `t` is 0, `b` when `t` is 1, and the matching point in between otherwise:

```
lerpf(0.2, 1.0, 0)   = 0.2
lerpf(0.2, 1.0, 0.5) = 0.6     (halfway between 0.2 and 1.0)
lerpf(0.2, 1.0, 1)   = 1.0
```

The formula behind it is simple: `a + (b - a) × t`. For the middle one: 0.2 + 0.8 × 0.5 = 0.6.

In a 2D game you'd put this brightness into a `CanvasModulate` node's colour; in 3D into a `DirectionalLight3D`'s `light_energy`.

## Your quest

1. `_process(delta)`: move `time_of_day` forward by `24.0 / day_length * delta` hours and wrap it with `fposmod`.
2. `brightness() -> float`: return the blended brightness from steps 1 to 4.
3. `is_night() -> bool`: `true` from 20:00 until 6:00 (20 or later, or before 6).

## Review

<details><summary>What does fposmod(25.0, 24.0) give?</summary>1.0: the clock wraps past midnight.</details>
<details><summary>What does lerpf(a, b, 0.5) give?</summary>The value halfway between a and b.</details>
<details><summary>Why use cos for brightness?</summary>It rises and falls smoothly in a loop, like the sun.</details>
