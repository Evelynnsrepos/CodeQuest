---
title: Building on a grid
xp: 25
---
# Place a wall

Base building in survival games snaps everything to a **grid**, so walls line up neatly. Two jobs:

1. turn a free position (where the mouse is) into a **grid cell**
2. remember which cells are taken

## World position to cell

Divide by the cell size and round **down**. With 32-pixel cells:

```
x = 70  →  70 / 32 = 2.19  →  floor → 2
y = 10  →  10 / 32 = 0.31  →  floor → 0
cell (2, 0)
```

"Round down" is `floor`. Round down, not to the nearest: 70 is inside the cell that **starts** at 64 (cell 2 spans 64 to 95). Try 90: 90 / 32 = 2.81 rounds to 3, but 90 is still in cell 2. Negative numbers work too: -5 / 32 = -0.16, floor gives -1, the cell just left of 0. ✔

`Vector2i` is a Vector2 with whole numbers, perfect for cells. `Vector2i(floor(70 / 32.0), floor(10 / 32.0))` is `(2, 0)`. Godot has a shortcut: `Vector2i((position / cell_size).floor())`.

## Cell back to world

To place the wall, go back: multiply the cell by the cell size. Cell `(2, 0)` starts at `(64, 0)`.

## Remembering taken cells

A Dictionary with cells as keys: `occupied[Vector2i(2, 0)] = "wall"`. Checking a cell is then `occupied.has(cell)`, which is fast even with thousands of buildings. (`TileMapLayer`, Godot's tile node, uses the same cell idea: `local_to_map()` and `map_to_local()`.)

## Your quest

1. `to_cell(world: Vector2) -> Vector2i` turns a world position into a cell.
2. `place(thing: String, world: Vector2) -> bool`: if that cell is free, store `thing` there and return `true`; otherwise return `false`.
3. `cell_to_world(cell: Vector2i) -> Vector2` returns the cell's top-left corner.
