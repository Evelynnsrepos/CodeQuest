---
title: Jumping to an exact height
xp: 30
---
# How high is a jump?

A jump is just a quick **upward speed**. Up is **negative y** in 2D, so a jump sets `velocity.y` to a negative number, and gravity (from lesson 1) slowly turns it around until the player falls again.

```gdscript
if Input.is_action_just_pressed("ui_accept") and is_on_floor():
	velocity.y = jump_velocity
```

`is_action_just_pressed` is true only on the **one frame** the key goes down, so holding the key doesn't jump again and again. The `is_on_floor()` part stops jumping in mid-air.

## Picking the jump speed from the height you want

Level designers think in **heights** ("the player can reach a 64-pixel ledge"), not in speeds. Physics gives a formula that turns one into the other. Let's build it step by step.

**Step 1.** Going up, gravity removes `g` from your speed every second. You start at speed `v` and stop at the top, so the trip up takes

```
time = v ÷ g
```

**Step 2.** Your speed drops evenly from `v` to `0`, so your **average** speed on the way up is halfway: `v ÷ 2`.

**Step 3.** Distance is average speed times time:

```
height = (v ÷ 2) × (v ÷ g) = v² ÷ (2 × g)
```

**Step 4.** We know the height and want `v`, so turn the formula around. Multiply both sides by `2 × g`, then take the square root (`√`, "which number times itself gives this?"):

```
v² = 2 × g × height
v  = √(2 × g × height)
```

Let's try it with `g = 980` and `height = 64`:

```
2 × 980 × 64 = 125440
√125440 ≈ 354.2
```

So the player needs `354.2` px/s upwards, which is `velocity.y = -354.2` (negative = up). In GDScript, `sqrt(x)` is the square root:

```gdscript
var jump_velocity := -sqrt(2.0 * gravity * jump_height)
```

Now you can change `jump_height` and the speed follows. That's how designers tune games.

## Your quest

1. Work out `jump_velocity` from `jump_height` and `gravity` with the formula (don't forget the minus sign).
2. In `_physics_process`, jump when `ui_accept` (Space or Enter) is just pressed **and** the player is on the floor.

The check measures your jump: its top should be about 64 pixels above the floor, and pressing jump in mid-air must do nothing.
