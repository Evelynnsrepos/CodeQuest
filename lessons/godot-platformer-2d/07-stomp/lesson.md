---
title: Stomp or get hurt
xp: 25
---
# Jumping on heads

When the player touches an enemy, two different things can happen:

- the player lands **on top**: the enemy is defeated and the player bounces up
- anything else: the player gets hurt

How do we know it's "on top"? Two questions, both about the y axis (remember, y grows **downwards**):

1. **Is the player falling?** `velocity.y > 0`.
2. **Are the player's feet above the enemy's middle?** The player is higher when its y is **smaller**. So we check `position.y < enemy.position.y - margin`. The margin (`8` here) makes sure the player is clearly above, not just touching the enemy's side.

```
      player  (y = 100)        y = 100 is less than 120 - 8 = 112, so: above ✔
      enemy   (y = 120)
```

In a real game, an `Area2D` on the player (its "hurtbox") would call this function from `body_entered`.

## Your quest

Write `touch_enemy(enemy: Node2D) -> String`:

- **Stomp**: if the player is falling **and** `position.y < enemy.position.y - 8`: remove the enemy with `queue_free()`, set `velocity.y` to `bounce_velocity`, and return `"stomp"`.
- **Hurt**: otherwise, lower `health` by 1 and return `"hurt"`.
