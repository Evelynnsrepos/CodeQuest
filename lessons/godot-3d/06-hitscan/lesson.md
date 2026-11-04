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

<svg viewBox="0 0 420 170" width="100%" style="max-width:420px" role="img" aria-label="A hitscan ray from the gun along its forward direction: the first body it touches is hit, anything behind is not"><defs><marker id="ahhs6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahhse5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker><marker id="ahhs30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ahhsd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker></defs><rect x="30.0" y="100.0" width="40.0" height="16.0" fill="#6c4cf5" rx="2"/><text x="50.0" y="136.0" font-size="11" fill="#6c4cf5" text-anchor="middle">gun</text><line x1="70.0" y1="108.0" x2="400.0" y2="108.0" stroke="#d97706" stroke-width="1.5" stroke-dasharray="5 4"/><text x="395.0" y="98.0" font-size="11" fill="#d97706" text-anchor="end">max_range</text><rect x="200.0" y="80.0" width="26.0" height="56.0" fill="#e5484d" rx="2"/><text x="213.0" y="152.0" font-size="11" fill="#e5484d" text-anchor="middle">first hit</text><circle cx="200.0" cy="108.0" r="4" fill="#e5484d"/><rect x="300.0" y="80.0" width="26.0" height="56.0" fill="#e5484d" opacity="0.35" rx="2"/><text x="313.0" y="152.0" font-size="11" fill="currentColor" text-anchor="middle">not hit</text><line x1="70.0" y1="108.0" x2="196.0" y2="108.0" stroke="#e5484d" stroke-width="2.5" marker-end="url(#ahhse5484d)"/><text x="210.0" y="30.0" font-size="11" fill="currentColor" text-anchor="middle">from = gun position, to = from + forward × max_range</text><text x="210.0" y="48.0" font-size="11" fill="currentColor" text-anchor="middle">forward is −basis.z</text></svg>

## Your quest

This script is the gun, a `Node3D` that faces forward. Write `shoot() -> Node`:

1. Build the ray from the gun's `global_position`, `max_range` metres along its forward.
2. Ask the space state for the first hit.
3. If something was hit and it has `take_damage`, call `take_damage(damage)`.
4. Return the collider, or `null` if nothing was hit.

## Review

<details><summary>What is hitscan?</summary>Shooting by casting a ray and hitting the first thing it touches, instantly.</details>
<details><summary>What does intersect_ray return when nothing is hit?</summary>An empty dictionary.</details>
