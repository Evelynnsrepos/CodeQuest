---
title: Scenes and instancing
xp: 20
hint: coin_scene.instantiate() makes a new copy of the scene.
hint: Set its position to spot, add_child(coin), then return coin.
---
# One bullet, a thousand copies

> **Warm-up:** You made one coin. How do you get 100 of them without building each by hand?

In Godot you build a thing once, like a bullet, an enemy or a coin, and save it as its own **scene** (a `.tscn` file). A scene is a little tree of nodes: a bullet might be an `Area2D` with a `Sprite2D` and a `CollisionShape2D` under it.

Then the game makes as many copies, called **instances**, as it needs:

```gdscript
@export var bullet_scene: PackedScene

func shoot():
	var bullet := bullet_scene.instantiate()
	bullet.position = position
	get_parent().add_child(bullet)
```

Two new things here:

- `PackedScene` is a saved scene, ready to be copied. `instantiate()` makes one copy.
- `@export` shows the variable in Godot's **Inspector**. In the editor you drag `bullet.tscn` onto that slot, so the script never needs to know the file name. You can also write `preload("res://bullet.tscn")` instead.

In CodeQuest there are no `.tscn` files, so the checks fill in `coin_scene` for you, just like dragging it into the Inspector.

## Your quest

Write `spawn_at(spot: Vector2) -> Node`:

1. Make an instance of `coin_scene`.
2. Put it at `spot`.
3. Add it as a child of this node.
4. Return it, so the caller can use it.

## Review

<details><summary>What is a PackedScene?</summary>A saved scene you can make copies of with instantiate().</details>
<details><summary>What does @export do?</summary>Shows the variable in the Inspector, so you can drag a scene into it.</details>
