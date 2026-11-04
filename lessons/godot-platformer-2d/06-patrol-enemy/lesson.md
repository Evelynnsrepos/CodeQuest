---
title: A patrolling enemy
xp: 30
---
# Back and forth

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

## Your quest

The ray is created for you. In `_physics_process`, before moving:

1. If the enemy is on a wall **or** the ray isn't colliding, flip `direction`, move the ray to the new front (`16 * direction`) and force a ray update.
2. Set `velocity.x` to `direction * speed`.

The check puts the enemy on a platform with a wall at one end and a drop at the other. It must keep patrolling without falling off.
