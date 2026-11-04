---
title: Project: 3D first-person shooter
xp: 40
hint: cycle: current = posmod(current + step, weapons.size())
hint: select: only change current if 0 <= index < weapons.size(). current_damage returns weapons[current].damage.
---
# Build it: a first-person shooter

> **Warm-up:** You have 3 weapons and scroll past the last one. What should happen?

> ✅ Tick the boxes as you go. Your ticks are saved on this device, so you can stop and come back any time.

Uses **Into 3D** lessons 2, 3, 5, 6 and 8, plus the ammo and waves from 2D Shooter.

## 1. The player

```
Player (CharacterBody3D)        ← walk with lesson 3's basis movement (strafe with input.x)
├── CollisionShape3D            ← CapsuleShape3D
└── Head (Node3D)               ← lesson 5's mouse look; place it at eye height (y ≈ 1.6)
    └── Camera3D
        └── Gun (Node3D)        ← lesson 6's hitscan + 2D Shooter's ammo
            └── GunModel
```

In `_ready()`: `Input.mouse_mode = Input.MOUSE_MODE_CAPTURED`. Free it again with Esc, or you can't close the window!

**Tick when done:**

- [ ] Player with capsule, head at eye height, camera and gun
- [ ] Mouse captured in _ready(), Esc frees it
- [ ] Mouse look and walking work (F5)

## 2. Enemies

```
Enemy (CharacterBody3D)         ← lesson 8's hunt(), health and take_damage()
├── CollisionShape3D
├── MeshInstance3D
└── NavigationAgent3D           ← walks around walls
```

Put the level geometry under a `NavigationRegion3D` and click **Bake NavigationMesh**. In `hunt()`, aim at `$NavigationAgent3D.get_next_path_position()` instead of the player directly.

**Tick when done:**

- [ ] Enemy scene with hunt(), health and take_damage()
- [ ] NavigationRegion3D baked; enemies walk around walls

## 3. Feel

Shooters live on feedback: a muzzle flash (a `GPUParticles3D` with **One Shot**), a sound (`AudioStreamPlayer3D`), a small camera kick (rotate the head up a little and ease it back with `lerpf`), and a hit marker on the HUD when `shoot()` returns something with `take_damage`.

**Tick when done:**

- [ ] Muzzle flash
- [ ] Shot sound
- [ ] Camera kick
- [ ] Hit marker on the HUD

## 4. Weapon switching (your quest)

The player carries a list of weapons. The mouse wheel steps through them, and number keys pick one directly.

Stepping past the last weapon should **wrap** to the first, and stepping back from the first to the last. `posmod(a, b)` is the whole-number version of `fposmod` from the day-night lesson:

```
posmod(3, 3)  = 0      (past the end → back to the start)
posmod(-1, 3) = 2      (before the start → the last one)
posmod(1, 3)  = 1
```

Write:

1. `cycle(step: int)`: move `current` by `step` (1 for wheel down, -1 for wheel up) and wrap it.
2. `select(index: int)`: pick that weapon, but ignore an `index` that doesn't exist (a player pressing 7 with 3 weapons).
3. `current_damage() -> int`: the current weapon's `damage`.

**Tick when done:**

- [ ] Mouse wheel and number keys switch weapons
- [ ] Shooting uses current_damage()

## Review

<details><summary>What does posmod(-1, 3) give?</summary>2, so stepping back from the first weapon wraps to the last.</details>
<details><summary>Why check the index in select?</summary>So pressing 9 with only 3 weapons doesn't crash.</details>
