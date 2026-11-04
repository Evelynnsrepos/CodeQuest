---
title: A HUD with Control nodes
xp: 20
hint: score_label.text = "Score: %d" % score
hint: health_bar.max_value = max_health, then health_bar.value = health.
---
# Score: 9001

> **Warm-up:** What are the first two things you look at on a game's screen, besides the game itself?

Menus, health bars and score counters are built from **Control** nodes, Godot's UI nodes. Unlike `Node2D`, they're laid out with anchors and containers so they fit any screen size. A few you'll use all the time:

| Node | Shows |
| --- | --- |
| `Label` | text |
| `ProgressBar` | a bar from `min_value` to `max_value`, e.g. health |
| `Button` | a clickable button (emits `pressed`) |
| `VBoxContainer` / `HBoxContainer` | stacks children vertically / horizontally |

To keep the HUD on screen while the camera moves, put it under a `CanvasLayer`.

The HUD shouldn't go looking for the player every frame. Instead, the player **emits signals** (like `health_changed` from the signals lesson) and the HUD **listens**:

```gdscript
player.health_changed.connect(hud.on_health_changed)
```

This way the player doesn't need to know the HUD exists, and you can delete or redesign the HUD without touching the player.

## Your quest

The HUD (`extends VBoxContainer`) builds its own `Label` and `ProgressBar` in `_ready()`, already written for you. Write the two listeners:

1. `on_score_changed(score: int)` sets the label's text to `Score: ` followed by the number, e.g. `Score: 42`.
2. `on_health_changed(health: int, max_health: int)` sets the bar's `max_value` to `max_health` and its `value` to `health`.

## Review

<details><summary>Which node shows text in the UI?</summary>Label.</details>
<details><summary>Why set max_value before value?</summary>A ProgressBar clamps value to max_value, so a bigger health would be cut off.</details>
