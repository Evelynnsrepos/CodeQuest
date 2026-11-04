---
title: Checkpoints and lives
xp: 20
hint: In die(): lives -= 1 first. If lives > 0, set position = checkpoint and velocity = Vector2.ZERO.
hint: Else game_over.emit(). In _physics_process: if position.y > death_y: die().
---
# Try again from here

> **Warm-up:** What should happen when you fall into a pit in a platformer?

When the player falls into a pit or runs out of health, the game sends them back to the last **checkpoint**. Lose all your **lives** and it's game over.

The player remembers the checkpoint as a `Vector2`. A checkpoint flag in the level is an `Area2D` that calls `set_checkpoint(its position)` when the player walks through it.

Falling into a pit is easy to detect: if `position.y` is greater than a `death_y` line far below the level, the player fell out of the world.

`velocity = Vector2.ZERO` stops all movement, so the player doesn't respawn while still falling at full speed.

## Your quest

1. `set_checkpoint(spot: Vector2)` stores `spot` in `checkpoint`.
2. `die()` takes away one life. If lives are left, move the player back to `checkpoint` and stop it. If no lives are left, emit `game_over`.
3. In `_physics_process`, call `die()` when `position.y > death_y`.

## Review

<details><summary>Why set velocity to zero when respawning?</summary>Otherwise the player keeps the falling speed and drops straight back down.</details>
<details><summary>How do you notice a fall into a pit?</summary>Check if position.y is bigger than a death line below the level.</details>
