---
title: Project: 2D top-down shooter
xp: 40
hint: pow(0.85, wave - 1) shrinks each wave. Multiply it by start_interval.
hint: Wrap it in maxf(..., min_interval). game_over: if score > high_score, store it and return true.
---
# Build it: a top-down shooter

> **Warm-up:** What makes a wave shooter get harder over time?

> ✅ Tick the boxes as you go. Your ticks are saved on this device, so you can stop and come back any time.

All the pieces come from this course. A wave-survival arena shooter is a great first shooter: one screen, endless replay.

## 1. Set up

- [ ] Input Map: `move_left/right/up/down` (WASD) and `shoot` (left mouse button: in the Input Map, click **+**, then pick **Mouse Buttons → Left**).
- [ ] Art: Kenney's *Top-down Shooter* pack.

## 2. Scenes

```
Player (CharacterBody2D)        ← move with Input.get_vector, aim (lesson 1),
├── Sprite2D                       gun (3), i-frames (7), ammo (8)
├── CollisionShape2D
└── Muzzle (Marker2D)           ← a Marker2D marks the gun tip visually

Bullet (Area2D)                 ← lessons 2 and 4
├── Sprite2D
└── CollisionShape2D

Enemy (CharacterBody2D)         ← chase from Basics 2, take_damage + died signal
├── Sprite2D
└── CollisionShape2D

Arena (Node2D)                  ← the main scene
├── TileMapLayer (floor and walls)
├── Player
├── WaveManager (Node)          ← lessons 5 and 6
└── HUD (CanvasLayer)           ← the HUD lesson from Basics 2
```

With a `Marker2D` you can use `$Muzzle.global_position` instead of computing the muzzle point.

Turn on **Debug → Visible Collision Shapes** while testing. It shows every hitbox.

**Tick when done:**

- [ ] Player scene with Sprite2D, CollisionShape2D and a Muzzle marker
- [ ] Bullet scene (Area2D) from lessons 2 and 4
- [ ] Enemy scene that chases and has take_damage and died
- [ ] Arena scene with walls, the player, a WaveManager and the HUD
- [ ] Visible Collision Shapes turned on, and you can shoot an enemy (F5)

## 3. Difficulty that ramps up (your quest)

Linear growth (lesson 6) is fine for enemy *count*. For the time between spawns, games often use **exponential decay**: each wave multiplies the time by the same number, like 0.85. It drops fast at first and then levels off.

`pow(a, n)` means "a multiplied by itself n times": `pow(0.85, 2) = 0.85 × 0.85 = 0.7225`. So:

```
interval(wave) = start_interval × 0.85^(wave − 1)

wave 1: 2.0 × 0.85⁰ = 2.0 × 1        = 2.0 s    (anything to the power 0 is 1)
wave 2: 2.0 × 0.85¹ = 2.0 × 0.85     = 1.7 s
wave 3: 2.0 × 0.85² = 2.0 × 0.7225   = 1.445 s
```

It would keep shrinking towards 0, so we put a floor under it with `maxf(..., min_interval)`, else wave 30 becomes a wall of enemies.

Write:

1. `spawn_interval(wave: int) -> float` with the formula and the `min_interval` floor.
2. `game_over(score: int) -> bool`: if `score` beats `high_score`, store it and return `true` (show "New high score!"), otherwise return `false`. Saving it to a file comes in the Survival systems course (the save lesson).

**Tick when done:**

- [ ] WaveManager waits spawn_interval(wave) between enemies
- [ ] Game over screen shows "New high score!" when game_over() returns true

## Review

<details><summary>What does pow(0.85, 2) mean?</summary>0.85 x 0.85 = 0.7225.</details>
<details><summary>Why put a floor under the spawn interval?</summary>Otherwise it keeps shrinking towards 0 and later waves become impossible.</details>
