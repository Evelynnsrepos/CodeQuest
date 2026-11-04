---
title: Press E to interact
xp: 25
hint: looking_at: if ray.is_colliding() and ray.get_collider().has_method("interact"), return the collider, else null.
hint: prompt_text and try_interact both start with var thing := looking_at() and handle null first.
---
# Chop the tree, open the chest

> **Warm-up:** How does a game know which door you're looking at?

Survival games are full of things you look at and use: trees, chests, doors, campfires. The usual way is a **RayCast3D** on the camera, pointing a couple of metres forward. Whatever it touches is what you're looking at.

```gdscript
var ray := RayCast3D.new()
ray.target_position = Vector3(0, 0, -2.5)   # 2.5 m forward, in the ray's own space
```

Unlike the query in the last lesson, a `RayCast3D` node updates **every physics frame** by itself, which is exactly what you want for showing a "Press E" prompt while you look at something.

- `ray.is_colliding()`: is it touching anything?
- `ray.get_collider()`: the node it touches

Each interactable thing gets an `interact(player)` method, and some also a `prompt` text like `"Chop tree"`. The player doesn't need to know what a chest or a tree is: duck typing again.

In a real project you'd add an **interact** action in *Project Settings → Input Map* (bound to E) and call `try_interact()` from `_unhandled_input` when `event.is_action_pressed("interact")`.

## Your quest

The ray is set up for you. Write:

1. `looking_at() -> Node`: the collider if the ray is colliding **and** the collider has an `interact` method, otherwise `null`.
2. `prompt_text() -> String`: `"[E] "` followed by the thing's `prompt` (e.g. `[E] Chop tree`), or `""` when you're not looking at anything usable.
3. `try_interact() -> bool`: call `interact(self)` on what you're looking at and return `true`, or return `false` if there's nothing.

## Review

<details><summary>What does a RayCast3D node do?</summary>Checks every physics frame whether a line from it hits something.</details>
<details><summary>Why use has_method("interact")?</summary>So any object (door, tree, chest) can be usable just by having that function.</details>
