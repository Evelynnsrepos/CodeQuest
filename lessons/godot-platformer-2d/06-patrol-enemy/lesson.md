---
title: A patrolling enemy
xp: 30
hint: The flip condition is: is_on_floor() and (is_on_wall() or not ledge_ray.is_colliding()).
hint: When flipping: direction *= -1, ledge_ray.position.x = 16 * direction, ledge_ray.force_raycast_update().
---
# Back and forth

> **Warm-up:** How would an enemy know it's about to walk off a cliff?

The classic platformer enemy walks until it hits a wall or reaches the edge of a platform, then turns around. It needs two senses:

1. **"Did I bump into a wall?"** `CharacterBody2D` tells you after `move_and_slide()` with `is_on_wall()`.
2. **"Is there ground ahead of me?"** For this we use a **RayCast2D**: an invisible line that reports whether it touches anything. We point it straight down, a little bit in front of the enemy's feet. If it hits nothing, there's a drop ahead.

```gdscript
var ray := RayCast2D.new()
ray.position = Vector2(16, 0)        # 16 px in front of the enemy
ray.target_position = Vector2(0, 40) # 40 px down from there
add_child(ray)

if not ray.is_colliding():
	print("no ground ahead!")
```

`direction` is `1` (walking right) or `-1` (walking left). Flipping it is just `direction *= -1`, because `1 × -1 = -1` and `-1 × -1 = 1`.

When the enemy turns, the ray must move to the **other side**, so it always looks ahead: `ray.position.x = 16 * direction`. A ray only updates on the next physics frame, so call `ray.force_raycast_update()` after moving it.

In the editor you'd add the RayCast2D as a child node and drag its arrow; it shows up as a line when you turn on **Debug → Visible Collision Shapes**.

<svg viewBox="0 0 420 240" width="100%" style="max-width:420px" role="img" aria-label="A patrolling enemy with a ray pointing down just ahead; when the ray hits nothing there is a drop and the enemy turns"><defs><marker id="ahpe6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahpee5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker><marker id="ahpe30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ahped97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker></defs><rect x="40.0" y="140.0" width="260.0" height="14.0" fill="currentColor" opacity="0.35" rx="2"/><rect x="40.0" y="60.0" width="14.0" height="80.0" fill="currentColor" opacity="0.35" rx="2"/><text x="47.0" y="52.0" font-size="11" fill="currentColor" text-anchor="middle">wall</text><rect x="230.0" y="110.0" width="26.0" height="30.0" fill="#e5484d" rx="2"/><line x1="256.0" y1="125.0" x2="280.0" y2="125.0" stroke="#e5484d" stroke-width="2" marker-end="url(#ahpee5484d)"/><text x="280.0" y="104.0" font-size="11" fill="#e5484d" text-anchor="middle">direction = 1</text><line x1="259.0" y1="125.0" x2="259.0" y2="165.0" stroke="#d97706" stroke-width="2" stroke-dasharray="5 4"/><circle cx="259.0" cy="165.0" r="3.5" fill="#d97706"/><text x="270.0" y="186.0" font-size="11" fill="#d97706" text-anchor="middle">ledge ray: hits the floor = keep going</text><line x1="300.0" y1="140.0" x2="300.0" y2="200.0" stroke="currentColor" stroke-width="1" stroke-dasharray="5 4" opacity="0.5"/><text x="330.0" y="150.0" font-size="11" fill="currentColor" text-anchor="start">drop</text><text x="170.0" y="225.0" font-size="11" fill="currentColor" text-anchor="middle">at the edge the ray hits nothing, so the enemy turns around</text></svg>

## Your quest

The ray is created for you. In `_physics_process`, before moving:

1. If the enemy is on a wall **or** the ray isn't colliding, flip `direction`, move the ray to the new front (`16 * direction`) and force a ray update.
2. Set `velocity.x` to `direction * speed`.

The check puts the enemy on a platform with a wall at one end and a drop at the other. It must keep patrolling without falling off.

## Review

<details><summary>What does the ledge ray point at?</summary>Down, just in front of the enemy: if it hits nothing, there's a drop ahead.</details>
<details><summary>Why call force_raycast_update() after moving the ray?</summary>Rays update once per physics frame; forcing it gives the new answer straight away.</details>
