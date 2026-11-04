---
title: Camera-relative movement
xp: 30
---
# Up means "away from the camera"

In 3D platformers and third-person games, the camera orbits around the player, and **up always means "away from the camera"**, whatever way the character faces. The character then turns to face where it's walking.

So we use the **camera's** turn instead of the player's. Only its sideways turn (the "yaw", around the y axis) matters: if the camera tilts down to look at the player, we still want to walk along the floor, not into it.

`Basis(Vector3.UP, yaw)` builds a basis that's turned by `yaw` around the up axis, so this is the same multiplication as last lesson:

```gdscript
var direction := Basis(Vector3.UP, camera_yaw) * Vector3(input.x, 0, input.y)
```

## Facing the way you walk

`look_at(target)` turns a node so its forward (-z) points at `target`. To face along `direction`, look at a point one step ahead:

```gdscript
look_at(global_position + direction)
```

Only do this while actually moving. `look_at` at your own position has no direction to face and Godot prints an error.

In a real scene the camera usually sits on a `SpringArm3D` (it pulls the camera in when a wall is in the way), and `camera_yaw` is that arm's `global_rotation.y`.

## Your quest

1. `move_direction(input: Vector2, camera_yaw: float) -> Vector3`: the world direction for this input, relative to the camera yaw.
2. `face(direction: Vector3)`: if `direction` isn't zero (`direction.length() > 0`), turn to face it with `look_at`.
