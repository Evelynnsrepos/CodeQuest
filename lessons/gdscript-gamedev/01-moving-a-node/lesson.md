---
title: Moving a node
xp: 15
---
# Make it move

In Godot, game objects are **nodes**. A `Node2D` has a `position` (a `Vector2` with `x` and `y`).

Godot calls `_process(delta)` on every frame. `delta` is the time since the last frame in seconds, about `0.016` at 60 FPS. Multiplying by `delta` makes movement the same speed on fast and slow computers.

```gdscript
extends Node2D

var velocity := Vector2(50, 0)   # 50 pixels per second to the right

func _process(delta):
	position += velocity * delta
```

From here on, your script is a real Godot node in a real scene. **Run** loads it into the scene (anything you `print` shows up). **Submit** plays it through the checks, which call your functions the way the engine would.

## Your quest

Your node has `velocity := Vector2(100, 0)`. Fill in `_process(delta)` so the node moves by `velocity` every second.

After half a second (`_process(0.5)`), the node should be at `(50, 0)`.
