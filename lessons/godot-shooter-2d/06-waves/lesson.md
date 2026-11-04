---
title: Waves
xp: 25
---
# Here comes wave 3

Wave shooters follow a loop: spawn a wave, wait until every enemy is dead, then start a bigger wave. The wave manager doesn't need to know *how* enemies die. It only needs to hear about it, so each enemy emits a `died` signal and the manager listens.


The difficulty formula: wave `n` has `3 + 2 × n` enemies. Wave 1 has 5, wave 2 has 7, wave 3 has 9. Each wave adds 2. This kind of steady growth is called **linear**: draw it on a chart and it's a straight line.

## Your quest

`spawn_enemy()` is written for you: it creates an enemy that has a `died` signal and returns it. Write:

1. `start_wave()`: add 1 to `wave`, then spawn `3 + 2 * wave` enemies. Connect each enemy's `died` signal to `_on_enemy_died`, and set `alive` to the number spawned.
2. `_on_enemy_died()`: lower `alive` by 1. When it reaches `0`, emit `wave_cleared` with the wave number.
