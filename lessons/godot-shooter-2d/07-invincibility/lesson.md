---
title: Invincibility frames
xp: 20
hint: take_damage: if invincible_time > 0 return; otherwise lower health and set invincible_time = invincible_duration.
hint: In _process: count invincible_time down with maxf(..., 0.0). While it's above 0, visible = int(invincible_time * 10) % 2 == 0; else visible = true.
---
# Blink blink

> **Warm-up:** Why do characters blink for a moment after getting hit?

If five enemies touch you at once, losing all your health in one frame feels unfair. Most games give the player a short **invincibility** window after each hit (often called **i-frames**), and make the sprite blink so you can see it.

It's the cooldown pattern once more: `invincible_time` counts down in `_process`, and while it's above zero, damage is ignored.

## Blinking

To blink, the sprite turns invisible and visible a few times a second. Here's a neat trick with the remaining time:

```gdscript
visible = int(invincible_time * 10) % 2 == 0
```

Step by step, with `invincible_time` going down from 1.0:

- `invincible_time * 10` turns 0.95 s into 9.5, 0.85 s into 8.5, and so on.
- `int(...)` cuts off the decimals: 9, 8, 7...
- `% 2` is the **remainder** after dividing by 2: 9 → 1, 8 → 0, 7 → 1. It flips between 0 and 1.
- `== 0` turns that into true, false, true... So the player is visible every other tenth of a second.

When the invincibility ends, make sure the player is visible again!

## Your quest

1. `take_damage(amount: int)`: if `invincible_time > 0`, ignore the hit. Otherwise lower `health` and set `invincible_time` to `invincible_duration`.
2. `_process(delta)`: count `invincible_time` down (not below 0). While it's above 0, blink with the trick above. Otherwise set `visible = true`.

## Review

<details><summary>What are invincibility frames for?</summary>So one touch can't hit you many frames in a row.</details>
<details><summary>How does the blink trick work?</summary>int(time x 10) changes every 0.1 s; % 2 turns that into on, off, on, off.</details>
