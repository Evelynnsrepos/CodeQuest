---
title: Project: 3D platformer
xp: 40
---
# Build it: a 3D platformer

Uses **Godot 6** lessons 1–4: a body that walks and jumps, moving relative to an orbiting camera.

## 1. Block out the level

Don't model anything yet. Use **CSG** nodes (`CSGBox3D`, `CSGCylinder3D`): boxes you can stretch in the editor. Tick **Use Collision** on each, and they're solid. Designers call this a **blockout**: get the jumps fun first, art later.

Add light and sky: in the 3D view's toolbar, the **sun** and **globe** buttons preview them. Click the **⋮** menu next to them and choose *Add Sun to Scene* and *Add Environment to Scene* to make them real nodes.

## 2. The player

```
Player (CharacterBody3D)        ← lesson 2's movement + lesson 4's camera-relative direction
├── CollisionShape3D            ← CapsuleShape3D
├── Model (Node3D)              ← a MeshInstance3D, or a character from Kenney / Quaternius
└── CameraPivot (Node3D)        ← top_level = true so it doesn't spin with the player
    └── SpringArm3D             ← Spring Length 5; pulls in when a wall is behind
        └── Camera3D
```

Rotate `CameraPivot` with the mouse (lesson 5's code, on the pivot) and pass `CameraPivot.global_rotation.y` as `camera_yaw`. Each frame, move the pivot to the player: `$CameraPivot.global_position = global_position`.

Give the `SpringArm3D` the player's RID to ignore: `$CameraPivot/SpringArm3D.add_excluded_object(get_rid())`.

The 2D tricks still work in 3D: coyote time, jump buffer, variable jump height (just flip the sign, up is +y).

## 3. Moving platforms (your quest)

Use an **AnimatableBody3D** for platforms: it moves by code and carries the player along.

Platforms that glide back and forth use a **sine wave**. You met cos in the day-night lesson; `sin` is the same wave, shifted so it starts at 0:

```
time:  0      ¼ period   ½ period   ¾ period   1 period
sin:   0      1          0          -1         0
```

So `sin(time / period × TAU)` swings smoothly from 0 up to 1, back through 0 down to -1 and back to 0, once every `period` seconds. Multiply by `distance` and it swings that many metres each way:

```
offset = axis × sin(time / period × TAU) × distance
position = start + offset
```

Example: `distance = 3`, `period = 4`, `axis = (1, 0, 0)`. At `time = 1` (a quarter period): `sin(1 / 4 × TAU) = sin(quarter turn) = 1`, so the platform is 3 m right of `start`. At `time = 3` it's 3 m left.

Write `_physics_process(delta)`: add `delta` to `time`, then set `position` with the formula.
