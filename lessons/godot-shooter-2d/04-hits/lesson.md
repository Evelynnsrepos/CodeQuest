---
title: Bullets that hit
xp: 25
---
# Ouch

A bullet is an `Area2D`, so it notices bodies with `body_entered` (from the collisions lesson). When it touches something:

- if the thing can take damage, damage it
- in any case, the bullet is used up: `queue_free()`

How do we know if "the thing can take damage"? We could check a group, but there's an even more flexible way: ask whether it **has the method**.

```gdscript
if body.has_method("take_damage"):
	body.take_damage(damage)
```

This is called **duck typing**: "if it has a `take_damage`, treat it like something that can be damaged". Enemies, crates and explosive barrels can all get a `take_damage` function, and the bullet works with every one of them without knowing what they are.

Walls usually don't have `take_damage`, so the bullet just disappears when it hits one.

One more thing: the player's own bullets shouldn't hurt the player. Here we skip any body in the `"player"` group. (Godot's **collision layers and masks**, in the Inspector under *Collision*, are another way: put the player and its bullets on layers that ignore each other.)

## Your quest

1. In `_ready()`, connect `body_entered` to `_on_body_entered`.
2. In `_on_body_entered(body)`: ignore bodies in the `"player"` group. For anything else, call `take_damage(damage)` if it has that method, and then `queue_free()` the bullet.
