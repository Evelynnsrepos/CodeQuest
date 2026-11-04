---
title: The gun
xp: 25
hint: Start with the cooldown: if _cooldown > 0 return null, else set _cooldown = cooldown_time.
hint: The muzzle is global_position + Vector2.from_angle(rotation) * muzzle_distance. Give the bullet the same rotation and add it to get_parent().
---
# Pew pew

> **Warm-up:** Why do bullets start at the tip of the gun, not in the middle of the player?

Time to put the pieces together: the **cooldown** from Basics 2, **instancing** a scene, and the **angle** maths.

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

## Review

<details><summary>Why add bullets to the parent instead of the player?</summary>Children move with their parent, so the bullets would turn when the player turns.</details>
<details><summary>How do you find the muzzle position?</summary>Start at the player and go muzzle_distance along the facing direction.</details>
