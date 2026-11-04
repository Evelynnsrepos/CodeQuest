---
title: Health and signals
xp: 20
hint: Start with: if health == 0: return. Then the hit can't emit died twice.
hint: health = max(health - amount, 0), then health_changed.emit(health), then emit died if health is 0.
---
# Shouting "I'm hurt!"

> **Warm-up:** When your health drops in a game, which other things need to know?

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

## Review

<details><summary>What is a signal for?</summary>A node announces that something happened; any number of other nodes can listen without the node knowing them.</details>
<details><summary>How do you send a signal with a value?</summary>health_changed.emit(health)</details>
