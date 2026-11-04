---
title: Collisions, areas and groups
xp: 25
---
# Picking up a coin

Godot's 2D physics has a few kinds of collision objects. You'll meet these the most:

| Node | What it's for |
| --- | --- |
| `CharacterBody2D` | things you move with code: the player, enemies |
| `StaticBody2D` | things that never move: floors, walls |
| `RigidBody2D` | things physics pushes around: crates, barrels |
| `Area2D` | invisible zones that **notice** overlaps but don't block: coins, spikes, bullets, trigger zones |

Every one of them needs a `CollisionShape2D` child that says how big it is (a circle, a rectangle...). In the editor you add one and draw the shape.

An `Area2D` emits `body_entered(body)` when a body moves into it, and `area_entered(area)` when another area does.

## Groups

How does the coin know that the thing touching it is the player, and not an enemy? With **groups**: labels you put on nodes.

```gdscript
# on the player
func _ready():
	add_to_group("player")

# on the coin
func _on_body_entered(body):
	if body.is_in_group("player"):
		print("got it!")
```

In the editor you add groups in the **Node → Groups** tab. `get_tree().get_nodes_in_group("enemies")` gives you every node in a group, which is handy for "freeze all enemies" or "count the enemies left".

## Removing a node

`queue_free()` deletes a node safely at the end of the frame. Use it for collected coins, dead enemies and bullets that hit something.

## Your quest

This script is a coin (`extends Area2D`). The check gives it a collision shape and drops bodies on it.

1. In `_ready()`, connect `body_entered` to `_on_body_entered`.
2. In `_on_body_entered(body)`: only if `body` is in the `"player"` group, emit `collected` and remove the coin with `queue_free()`. An enemy walking over the coin must not collect it.
