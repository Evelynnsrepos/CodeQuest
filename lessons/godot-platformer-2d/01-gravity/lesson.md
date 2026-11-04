---
title: Gravity
xp: 25
---
# What goes up...

Platformers use `CharacterBody2D` for the player. It has a built-in `velocity` (a `Vector2`, in pixels per second) and a method `move_and_slide()` that moves the body by its velocity **and stops it at walls and floors** instead of letting it pass through. Afterwards `is_on_floor()` tells you if it's standing on something.

Physics code goes in `_physics_process(delta)` instead of `_process`. Godot calls it exactly 60 times a second, so `delta` is always `1/60` ≈ `0.0167` s, which keeps jumps the same height every time.

## Gravity is a change of speed

Gravity doesn't move you at a fixed speed. It makes you fall **faster and faster**. Each second it adds `gravity` to your downward speed. With `gravity = 980` (pixels per second, per second):

| time | `velocity.y` (downward speed) |
| --- | --- |
| 0 s | 0 |
| 0.5 s | 490 |
| 1 s | 980 |
| 2 s | 1960 |

Remember that in 2D, **y points down**, so a positive `velocity.y` means falling.

Each physics frame only lasts `delta` seconds, so we add just that frame's share:

```gdscript
velocity.y += gravity * delta    # 980 × 0.0167 ≈ 16 more px/s every frame
```

## A speed limit

Real things stop speeding up when air resistance balances gravity: that top speed is called **terminal velocity**. Games copy this so long falls stay controllable. `minf(a, b)` gives the smaller of two numbers, so this keeps `velocity.y` at most `max_fall_speed`:

```gdscript
velocity.y = minf(velocity.y, max_fall_speed)
```

## Your quest

Write `_physics_process(delta)`:

1. If the player is **not** on the floor, add `gravity * delta` to `velocity.y`.
2. Limit `velocity.y` to `max_fall_speed`.
3. Call `move_and_slide()`.

The check drops your player onto a floor. It should speed up while falling, never go faster than `600`, and come to rest on the floor.
