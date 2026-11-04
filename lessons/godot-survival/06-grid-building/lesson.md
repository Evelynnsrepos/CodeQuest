---
title: Building on a grid
xp: 25
hint: to_cell: Vector2i((world / cell_size).floor()).
hint: place: get the cell, return false if occupied.has(cell), else store the thing and return true. cell_to_world is Vector2(cell * cell_size).
---
# Place a wall

> **Warm-up:** In a building game, why do walls snap into neat squares?

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

<svg viewBox="0 0 330 210" width="100%" style="max-width:330px" role="img" aria-label="A grid of 32-pixel cells: the point (70, 40) falls in cell (2, 1), whose top-left corner is (64, 32)"><defs><marker id="ahgb6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahgbe5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker><marker id="ahgb30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ahgbd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker></defs><line x1="40.0" y1="30.0" x2="40.0" y2="174.0" stroke="currentColor" stroke-width="1.5" opacity="0.4"/><line x1="88.0" y1="30.0" x2="88.0" y2="174.0" stroke="currentColor" stroke-width="1.5" opacity="0.4"/><line x1="136.0" y1="30.0" x2="136.0" y2="174.0" stroke="currentColor" stroke-width="1.5" opacity="0.4"/><line x1="184.0" y1="30.0" x2="184.0" y2="174.0" stroke="currentColor" stroke-width="1.5" opacity="0.4"/><line x1="232.0" y1="30.0" x2="232.0" y2="174.0" stroke="currentColor" stroke-width="1.5" opacity="0.4"/><line x1="280.0" y1="30.0" x2="280.0" y2="174.0" stroke="currentColor" stroke-width="1.5" opacity="0.4"/><line x1="40.0" y1="30.0" x2="280.0" y2="30.0" stroke="currentColor" stroke-width="1.5" opacity="0.4"/><line x1="40.0" y1="78.0" x2="280.0" y2="78.0" stroke="currentColor" stroke-width="1.5" opacity="0.4"/><line x1="40.0" y1="126.0" x2="280.0" y2="126.0" stroke="currentColor" stroke-width="1.5" opacity="0.4"/><line x1="40.0" y1="174.0" x2="280.0" y2="174.0" stroke="currentColor" stroke-width="1.5" opacity="0.4"/><text x="64.0" y="22.0" font-size="10" fill="currentColor" text-anchor="middle">x 0</text><text x="112.0" y="22.0" font-size="10" fill="currentColor" text-anchor="middle">x 1</text><text x="160.0" y="22.0" font-size="10" fill="currentColor" text-anchor="middle">x 2</text><text x="208.0" y="22.0" font-size="10" fill="currentColor" text-anchor="middle">x 3</text><text x="256.0" y="22.0" font-size="10" fill="currentColor" text-anchor="middle">x 4</text><text x="32.0" y="58.0" font-size="10" fill="currentColor" text-anchor="end">y 0</text><text x="32.0" y="106.0" font-size="10" fill="currentColor" text-anchor="end">y 1</text><text x="32.0" y="154.0" font-size="10" fill="currentColor" text-anchor="end">y 2</text><rect x="136.0" y="78.0" width="48.0" height="48.0" fill="#30a46c" opacity="0.3" rx="2"/><circle cx="145.0" cy="90.0" r="5" fill="#e5484d"/><text x="153.0" y="106.0" font-size="11" fill="#e5484d" text-anchor="start">mouse at (70, 40)</text><circle cx="136.0" cy="78.0" r="4" fill="#30a46c"/><text x="130.0" y="72.0" font-size="11" fill="#30a46c" text-anchor="end">corner (64, 32)</text><text x="160.0" y="196.0" font-size="11" fill="currentColor" text-anchor="middle">70 ÷ 32 = 2.19 → 2 and 40 ÷ 32 = 1.25 → 1, so cell (2, 1)</text></svg>

## Your quest

1. `to_cell(world: Vector2) -> Vector2i` turns a world position into a cell.
2. `place(thing: String, world: Vector2) -> bool`: if that cell is free, store `thing` there and return `true`; otherwise return `false`.
3. `cell_to_world(cell: Vector2i) -> Vector2` returns the cell's top-left corner.

## Review

<details><summary>Why floor() before turning into a cell?</summary>So -1 pixel lands in cell -1, not cell 0.</details>
<details><summary>How do you remember which cells are taken?</summary>A dictionary with the cell (Vector2i) as key.</details>
