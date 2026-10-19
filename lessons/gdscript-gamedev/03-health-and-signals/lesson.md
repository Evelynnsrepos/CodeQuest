---
title: Health and signals
xp: 20
---
# Shouting "I'm hurt!"

A **signal** lets a node announce that something happened without knowing who is listening. The health bar, sound effects and game-over screen can all connect to the same signal.

```gdscript
signal coin_collected(total)

func collect():
	coins += 1
	coin_collected.emit(coins)
```

Other nodes listen with `player.coin_collected.connect(_on_coin_collected)`.

## Your quest

The player has `signal health_changed(new_health)` and `signal died`. Write `take_damage(amount: int)`:

1. Lower `health` by `amount`, but never below `0`.
2. Emit `health_changed` with the new health.
3. Emit `died` only at the moment health reaches `0`, not again if the player is hit while already at 0.
