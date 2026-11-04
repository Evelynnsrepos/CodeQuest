---
title: Project: 2D survival game
xp: 40
---
# Build it: a top-down survival game

Everything from this course comes together here, with movement from Basics 2.

## 1. Scenes

```
World (Node2D)
├── TileMapLayer (ground)       ← grass, water, sand
├── CanvasModulate              ← day and night (lesson 5) colours the whole world
├── Resources (Node2D)          ← trees and rocks (lesson 4), scattered by your quest
├── Buildings (Node2D)          ← placed on the grid (lesson 6)
├── Creatures (Node2D)          ← wolves (lesson 8)
├── Player (CharacterBody2D)    ← stats (lesson 1), inventory (2), crafting (3)
└── UI (CanvasLayer)
    ├── StatBars                ← ProgressBars for health, hunger, thirst
    ├── Hotbar (HBoxContainer)  ← one TextureRect per inventory slot
    └── CraftMenu
```

Turn on **Y Sort Enabled** on the `World` node, so the player walks *behind* trees when above them and *in front* when below.

Hook up the day cycle: `$CanvasModulate.color = Color(b, b, b * 1.1)` with `b = brightness()` gives a slightly blue night.

Save the game every in-game morning, and load it in `_ready()` if `FileAccess.file_exists("user://save.json")`.

## 2. Scattering resources (your quest)

Placing 50 trees by hand is boring, and placing them **completely** at random puts some right on top of each other. The fix is simple: pick a random spot, and only keep it if it isn't too close to a spot you already have. Otherwise try again. This is called **rejection sampling**.

```
repeat until you have enough (or tried too often):
    spot = random point in the area
    if spot is at least min_gap away from every kept spot:
        keep it
```

The "tried too often" part matters: if the area is too small to fit everything, the loop would otherwise run forever and freeze the game.

A `Rect2` is a rectangle: `area.position` is its top-left corner and `area.size` its width and height. `randf_range(a, b)` gives a random float between a and b, so a random point inside is:

```gdscript
Vector2(randf_range(area.position.x, area.end.x), randf_range(area.position.y, area.end.y))
```

(`area.end` is `position + size`, the bottom-right corner.)

Write `scatter(count: int, area: Rect2, min_gap: float) -> Array` that returns up to `count` points inside `area`, each at least `min_gap` from all others. Give up after `count * 30` tries.
