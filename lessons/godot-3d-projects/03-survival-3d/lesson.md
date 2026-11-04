---
title: Project: 3D survival game
xp: 40
hint: In _ready: process_mode = Node.PROCESS_MODE_ALWAYS and visible = false.
hint: toggle_pause: get_tree().paused = not get_tree().paused, then visible = get_tree().paused.
---
# Build it: a 3D survival game

> **Warm-up:** If the game is paused, how can the pause menu still work?

> ✅ Tick the boxes as you go. Your ticks are saved on this device, so you can stop and come back any time.

The big one. Survival systems's systems don't care whether the world is 2D or 3D, so they carry over almost unchanged. Movement and looking come from Into 3D.

## 1. Pieces

| Part | From |
| --- | --- |
| first-person body and camera | Into 3D, lessons 3 and 5 |
| "Press E to chop" | Into 3D, lesson 7 |
| trees and rocks | Survival systems, lesson 4 (make them `StaticBody3D` with `interact()` calling `hit()`) |
| hunger, thirst, inventory, crafting | Survival systems, lessons 1–3 |
| sun and night | Survival systems, lesson 5: brightness → `DirectionalLight3D.light_energy`, and rotate the light: `rotation.x = -time_of_day / 24 × TAU` |
| wolves | Survival systems, lesson 8 for the decision, Into 3D lesson 8 to move |
| building | Survival systems, lesson 6 with a 3D grid: `Vector3i` and `(position / cell_size).floor()` |
| saving | Survival systems, lesson 7 (save `x`, `y` and `z` now) |

**Tick when done:**

- [ ] First-person body and camera
- [ ] Press E to chop trees and rocks
- [ ] Hunger, thirst, inventory and crafting
- [ ] Sun that moves and night
- [ ] Wolves
- [ ] Building on a 3D grid
- [ ] Saving with x, y and z

## 2. Terrain

For a first version, a big `CSGBox3D` or a `MeshInstance3D` with a `PlaneMesh` and a `StaticBody3D` is enough. Later, the free **Terrain3D** add-on (in the **AssetLib** tab) gives you sculpting and painting. For trees, use `MultiMeshInstance3D` when you have hundreds of them: it draws them all in one go.

**Tick when done:**

- [ ] Ground with collision
- [ ] Trees placed (MultiMeshInstance3D if there are hundreds)

## 3. The pause menu (your quest)

Every game needs a pause menu, and the inventory and crafting screens usually pause too.

`get_tree().paused = true` freezes the game: nodes stop getting `_process`, `_physics_process` and input. But the **menu** must keep working while everything else is frozen, or you could never unpause! Each node has a `process_mode`:

| `process_mode` | runs when... |
| --- | --- |
| `PROCESS_MODE_INHERIT` | same as its parent (the default) |
| `PROCESS_MODE_PAUSABLE` | only when not paused |
| `PROCESS_MODE_ALWAYS` | always, even when paused |
| `PROCESS_MODE_WHEN_PAUSED` | only while paused |

So the pause menu is `PROCESS_MODE_ALWAYS`. Its children inherit that, so its buttons work too. In the editor it's under **Process → Mode** in the Inspector.

In a first-person game, also free the mouse while paused so the player can click the buttons: `Input.mouse_mode = Input.MOUSE_MODE_VISIBLE`, and capture it again when resuming.

Write:

1. `_ready()`: set this node's `process_mode` to always, and hide the menu (`visible = false`).
2. `toggle_pause()`: flip `get_tree().paused` and show the menu exactly when the game is paused.

When you've built all six games, you've done what this course set out to do. Next, make one of them **yours**: a twist, a story, your own art. That's how every indie game starts.

**Tick when done:**

- [ ] Esc opens the pause menu and the game freezes behind it
- [ ] Resume button unpauses

## Review

<details><summary>What does get_tree().paused = true do?</summary>Stops _process, _physics_process and input for pausable nodes.</details>
<details><summary>Which process_mode keeps a menu working while paused?</summary>PROCESS_MODE_ALWAYS (or WHEN_PAUSED).</details>
