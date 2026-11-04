---
title: A 3D enemy that hunts you
xp: 30
hint: var flat := target - global_position, then flat.y = 0.
hint: If flat.length() > attack_range move with flat.normalized() * speed and look_at(Vector3(target.x, global_position.y, target.z)); else stop and attack(). Always move_and_slide().
---
# Footsteps behind you

> **Warm-up:** What does a 3D zombie need to know to walk towards you?

Time to combine the 3D tools: `ground_direction` from lesson 1, `look_at` from lesson 4 and `move_and_slide`.

The enemy walks towards the player **along the ground** (otherwise, if the player jumped, the enemy would try to fly). It stops when it's within `attack_range`, so it doesn't push into the player, and then calls `attack()`.

Facing the player: `look_at` a point at the player's x and z but the enemy's **own** height. Otherwise it tilts forward and backward when the player jumps:

```gdscript
look_at(Vector3(target.x, global_position.y, target.z))
```

For a real level with walls and obstacles, use a **NavigationAgent3D**: bake a navigation mesh on a `NavigationRegion3D`, set `agent.target_position = player.global_position`, and walk towards `agent.get_next_path_position()` instead of straight at the player. The movement code stays exactly the same.

## Your quest

Write `hunt(target: Vector3)`. `_physics_process` already calls it every frame with the player's position (in a game you'd set `target = player.global_position`).

1. Work out the flat distance and direction to the target (y ignored).
2. If farther than `attack_range`: set `velocity.x` and `velocity.z` from the direction times `speed`, and face the target.
3. Otherwise: stop (`velocity.x` and `velocity.z` to 0) and call `attack()`.
4. Always finish with `move_and_slide()`.

## Review

<details><summary>Why look at the target at your own height?</summary>So the enemy turns but doesn't tilt up or down.</details>
<details><summary>What does the enemy do inside attack range?</summary>Stops moving and attacks.</details>
