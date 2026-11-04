---
title: Project: 2D platformer
xp: 40
---
# Build it: a 2D platformer

You have every piece from **Godot 3**. This guide puts them together in the real Godot editor. Work through it with Godot open next to CodeQuest.

## 1. Set up the project

1. In the Project Manager click **Create**, name it, pick **Forward+** (or **Compatibility** for older PCs) and create.
2. **Project → Project Settings → Input Map**: add `move_left`, `move_right` and `jump` and bind keys (A/D/Space and the arrow keys). Use these names instead of `ui_left`... in your scripts.
3. Free art: [kenney.nl](https://kenney.nl) has free (CC0) platformer packs. Drag the folder into the **FileSystem** dock.
4. For crisp pixel art: **Project Settings → Rendering → Textures → Default Texture Filter → Nearest**.

## 2. The player scene

**Scene → New Scene**, then build this tree with the **+** button:

```
Player (CharacterBody2D)        ← script: lessons 1–5, 8, 9
├── AnimatedSprite2D            ← SpriteFrames: idle, run, jump, fall
├── CollisionShape2D            ← CapsuleShape2D or RectangleShape2D
└── Camera2D                    ← tick Position Smoothing
```

Add the player to the `player` group (**Node → Groups**). Save as `player.tscn`.

## 3. The level

```
Level1 (Node2D)
├── TileMapLayer                ← paint the ground
├── Player (instance)           ← drag player.tscn in
├── Enemies (Node2D)            ← patrol enemies from lesson 6
├── Coins (Node2D)              ← Area2D coins from Godot 2
├── Checkpoint (Area2D)         ← calls player.set_checkpoint()
└── Goal (Area2D)               ← the flag at the end
```

**TileMapLayer**: in the Inspector create a new **TileSet**, set its tile size (e.g. 16×16), then in the **TileSet** panel at the bottom drag your tile sheet in. To make tiles solid, add a **Physics Layer** to the TileSet and draw collision polygons on the tiles. Then paint in the **TileMap** panel.

Set the Camera2D's **Limit** values so it doesn't show past the level's edges.

## 4. The game manager (your quest)

Something has to remember the coins and which level comes next, even while levels change. In Godot that's an **Autoload**: a script that's always loaded. Add it in **Project Settings → Globals → Autoload**, name it `Game`, and any script can use `Game.collect_coin()`.

When the player reaches the Goal: `get_tree().change_scene_to_file(Game.next_level())`.

Write the manager:

1. `collect_coin()`: add 1 to `coins`. Every 100 coins gives an extra life: when `coins` reaches 100, add 1 to `lives` and set `coins` back to `0`.
2. `next_level() -> String`: move `current` to the next level and return its path from `levels`. After the last level, return `"res://win_screen.tscn"`.

## 5. Ship it

**Project → Export**, add a preset for your system, download the export templates when asked, and **Export Project**. Now you have a game other people can play.
