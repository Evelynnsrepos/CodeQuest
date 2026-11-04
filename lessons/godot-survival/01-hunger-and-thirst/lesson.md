---
title: Hunger and thirst
xp: 20
---
# Getting hungry

Survival games keep the player busy with **stats that drain over time**: hunger, thirst, warmth, stamina. Each one is a number that goes down a little every frame and is refilled by eating, drinking or resting.

"Goes down by `rate` per second" is the same `delta` trick as movement:

```gdscript
hunger -= hunger_rate * delta
```

Stats live between `0` and a maximum, so after every change we **clamp** them. `clampf(value, low, high)` keeps a number inside a range:

```gdscript
clampf(-3.0, 0.0, 100.0)    # 0.0   (too low, raised to 0)
clampf(42.0, 0.0, 100.0)    # 42.0  (fine, unchanged)
clampf(130.0, 0.0, 100.0)   # 100.0 (too high, lowered to 100)
```

When a stat is empty, the player starts losing health instead. That's what makes the player go find food.

## Your quest

1. In `_process(delta)`: lower `hunger` by `hunger_rate * delta` and `thirst` by `thirst_rate * delta`, clamped to `0`–`100`. Then, if either one is `0`, lower `health` by `starve_damage * delta` (once, even if both are empty).
2. `eat(amount: float)` adds to `hunger`, but never above `100`.
