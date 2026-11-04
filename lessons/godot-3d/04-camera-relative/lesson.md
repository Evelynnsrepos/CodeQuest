---
title: Camera-relative movement
xp: 30
hint: Basis(Vector3.UP, camera_yaw) is a turn around the up axis by the camera's yaw.
hint: Multiply it with Vector3(input.x, 0, input.y). In face, look_at(global_position + direction) when the length is above 0.
---
# Up means "away from the camera"

> **Warm-up:** In a third-person game, why does pressing up walk away from the camera, not always north?

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

<svg viewBox="0 0 380 280" width="100%" style="max-width:380px" role="img" aria-label="Seen from above: with the camera turned, pressing up walks the player away from the camera instead of north"><defs><marker id="ahcr6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahcre5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker><marker id="ahcr30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ahcrd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker></defs><line x1="180.0" y1="150.0" x2="180.0" y2="40.0" stroke="currentColor" stroke-width="1" stroke-dasharray="5 4" opacity="0.5"/><text x="180.0" y="32.0" font-size="11" fill="currentColor" text-anchor="middle">north (world −z)</text><rect x="222.5" y="218.8" width="24.0" height="18.0" fill="#d97706" rx="2"/><text x="234.5" y="253.8" font-size="11" fill="#d97706" text-anchor="middle">camera</text><line x1="234.5" y1="227.8" x2="183.4" y2="154.9" stroke="#d97706" stroke-width="1.5" stroke-dasharray="5 4"/><circle cx="180.0" cy="150.0" r="9" fill="#6c4cf5"/><line x1="180.0" y1="150.0" x2="134.1" y2="84.5" stroke="#6c4cf5" stroke-width="2.5" marker-end="url(#ahcr6c4cf5)"/><text x="122.7" y="83.6" font-size="11" fill="#6c4cf5" text-anchor="end">pressing ↑ walks here</text><text x="180.0" y="270.0" font-size="11" fill="currentColor" text-anchor="middle">↑ means away from the camera, not always north</text></svg>

## Your quest

1. `move_direction(input: Vector2, camera_yaw: float) -> Vector3`: the world direction for this input, relative to the camera yaw.
2. `face(direction: Vector3)`: if `direction` isn't zero (`direction.length() > 0`), turn to face it with `look_at`.

## Review

<details><summary>What is yaw?</summary>Turning left or right around the up axis.</details>
<details><summary>Why check direction.length() &gt; 0 before look_at?</summary>look_at with no direction has nothing to look at and gives an error.</details>
