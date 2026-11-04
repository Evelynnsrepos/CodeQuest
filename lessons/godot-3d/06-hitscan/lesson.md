---
title: Hitscan shooting
xp: 30
hint: Forward is -global_transform.basis.z. The end point is from + forward * max_range.
hint: PhysicsRayQueryParameters3D.create(from, to), then get_world_3d().direct_space_state.intersect_ray(query). An empty result means no hit.
---
# Bang, instantly

> **Warm-up:** Why do bullets in many shooters hit instantly instead of flying?

Fast guns in shooters usually don't fire a flying bullet. They **hitscan**: draw an invisible straight line from the gun and hit the first thing on it, instantly. That line is a **ray**.

## A ray from the camera

The ray starts at the camera and goes forward (`-basis.z`) for `max_range` metres:

```
from = global_position
to   = from + (-global_transform.basis.z) * max_range
```

(`global_transform` instead of `transform`, because the camera sits inside the head inside the player, and we need its direction in the **world**.)

## Asking the physics world

Godot's physics world answers ray questions through its **direct space state**:

```gdscript
var space := get_world_3d().direct_space_state
var query := PhysicsRayQueryParameters3D.create(from, to)
query.exclude = [player.get_rid()]       # don't hit yourself
var hit := space.intersect_ray(query)
```

`hit` is a Dictionary. It's **empty** when the ray hit nothing. Otherwise it has:

- `hit.collider`: the node that was hit
- `hit.position`: where (good for spawning a spark or bullet hole)
- `hit.normal`: the direction the surface faces at that point

Then use duck typing like the 2D bullets: `if hit.collider.has_method("take_damage")`.

There's also a `RayCast3D` node you can add in the editor, which updates every frame. A query like this is better for guns because it checks the exact moment you fire.

## Your quest

This script is the gun, a `Node3D` that faces forward. Write `shoot() -> Node`:

1. Build the ray from the gun's `global_position`, `max_range` metres along its forward.
2. Ask the space state for the first hit.
3. If something was hit and it has `take_damage`, call `take_damage(damage)`.
4. Return the collider, or `null` if nothing was hit.

## Review

<details><summary>What is hitscan?</summary>Shooting by casting a ray and hitting the first thing it touches, instantly.</details>
<details><summary>What does intersect_ray return when nothing is hit?</summary>An empty dictionary.</details>
