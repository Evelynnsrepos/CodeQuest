---
title: Walking and jumping in 3D
xp: 30
---
# A body in 3D

`CharacterBody3D` works just like `CharacterBody2D`: set `velocity`, call `move_and_slide()`, ask `is_on_floor()`. Godot's own **CharacterBody3D template** (the one you get when you attach a new script to a CharacterBody3D) looks almost like what you'll write here.

Three changes from 2D:

1. **Gravity lowers y**, because y points up now: `velocity.y -= gravity * delta`.
2. **A jump is a positive y speed**: `velocity.y = jump_velocity` with a positive number.
3. **The arrow keys move on the floor plane (x and z)**, not x and y.

`Input.get_vector()` still gives a `Vector2`. Its `x` is left/right, and its `y` is up/down on the keyboard, which is **-1 for up** (just like 2D). In 3D, "up arrow" should mean "forward", which is **-z**. So the input's `y` goes straight into `z`:

```
up arrow    → input = (0, -1)  → direction = (0, 0, -1)  forward ✔
right arrow → input = (1, 0)   → direction = (1, 0, 0)   right ✔
```

```gdscript
var input := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
var direction := Vector3(input.x, 0, input.y)
velocity.x = direction.x * speed
velocity.z = direction.z * speed
```

Only set `x` and `z` from the input, never `y`. That one belongs to gravity and jumping.

In the editor, a 3D character is a `CharacterBody3D` with a `CollisionShape3D` (usually a capsule) and a `MeshInstance3D` to see it. A `StaticBody3D` with a box shape makes a floor. The check builds both for you.

## Your quest

Write `_physics_process(delta)`:

1. When not on the floor, lower `velocity.y` by `gravity * delta`.
2. When `ui_accept` is just pressed on the floor, set `velocity.y` to `jump_velocity`.
3. Move on x and z from the arrow keys at `speed`.
4. `move_and_slide()`.
