---
title: First-person mouse look
xp: 30
hint: rotate_y(-event.relative.x * sensitivity) turns the body.
hint: head.rotation.x = clampf(head.rotation.x - event.relative.y * sensitivity, deg_to_rad(-89), deg_to_rad(89))
---
# Look around

> **Warm-up:** Why can't you look so far up in a first-person game that you flip upside down?

A first-person shooter turns with the mouse. The scene usually looks like this:

```
Player (CharacterBody3D)      ← turns left/right (yaw)
└── Head (Node3D)             ← tilts up/down (pitch)
    └── Camera3D
```

Why split it? If the whole body tilted up, "forward" would point into the sky and the player would try to walk upwards. With the split, the body only turns left/right, so the basis movement from lesson 3 still walks along the floor.

## Reading the mouse

Mouse movement arrives as an **input event**, not in `_process`. Godot calls `_unhandled_input(event)` for every event the UI didn't use:

```gdscript
func _unhandled_input(event):
	if event is InputEventMouseMotion:
		print(event.relative)    # how far the mouse moved, in pixels
```

To turn, multiply the pixels by a small `sensitivity` (radians per pixel):

- moving the mouse **right** (positive `relative.x`) should turn **right**. A positive y rotation turns *left*, so we subtract: `rotate_y(-event.relative.x * sensitivity)`.
- moving the mouse **down** (positive `relative.y`) should look **down**, which is a negative x rotation, so we subtract here too.

## Don't break your neck

Without a limit, moving the mouse up forever flips the camera upside down. **Clamp** the head's pitch between straight down and straight up. That's 90° each way, but we stop just short at 89°, because exactly 90° confuses some camera math. Work out the new pitch and clamp it in one go:

```gdscript
head.rotation.x = clampf(head.rotation.x - event.relative.y * sensitivity, deg_to_rad(-89), deg_to_rad(89))
```

Why not `head.rotate_x(...)` and clamp afterwards? Because a big turn could go past 180°, where angles wrap around to negative numbers, and the clamp would then snap the camera to the wrong side. Setting `rotation.x` directly keeps the number honest.

In the real game, also capture the mouse so it doesn't leave the window: `Input.mouse_mode = Input.MOUSE_MODE_CAPTURED` in `_ready()`.

## Your quest

The `Head` node is created for you. In `_unhandled_input(event)`, for `InputEventMouseMotion` events:

1. Turn the body left/right with `rotate_y`.
2. Tilt the head up/down by setting `head.rotation.x`, clamped to ±89°.

## Review

<details><summary>Why turn the body for left/right but only the head for up/down?</summary>Walking should follow where you face, but not tilt into the floor when you look down.</details>
<details><summary>Why clamp the head at 89 degrees?</summary>Past 90 the view flips over.</details>
