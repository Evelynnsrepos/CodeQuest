---
title: The gun
xp: 25
---
# Pew pew

Time to put the pieces together: the **cooldown** from Godot 2, **instancing** a scene, and the **angle** maths.

A bullet should appear at the **tip of the gun** (the "muzzle"), not in the middle of the player. The muzzle is `muzzle_distance` pixels in front of the player, in the direction it's facing:

```
muzzle = global_position + Vector2.from_angle(rotation) * muzzle_distance
```

For example the player at `(100, 100)` facing down (`PI / 2`) with `muzzle_distance = 20`:

```
Vector2.from_angle(PI / 2) = (0, 1)
(0, 1) × 20 = (0, 20)
(100, 100) + (0, 20) = (100, 120)
```

The bullet gets the player's `rotation`, so it flies the same way the player faces.

Add the bullet to the **level** (`get_parent()`), not to the player. A child moves and turns with its parent, so a bullet added to the player would swing around whenever the player turned!

## Your quest

Write `shoot() -> Node2D`:

1. If the cooldown is still running, return `null`.
2. Otherwise restart the cooldown, make a bullet from `bullet_scene`, place it at the muzzle with the player's rotation, add it to `get_parent()` and return it.

The `_process` cooldown countdown is already written.
