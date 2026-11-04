---
title: A creature with a mind
xp: 30
---
# Wolves

Remember `enum` and `match` from Basics 1? Here's where they shine. A wolf in a survival game might:

| state | does | switches when |
| --- | --- | --- |
| `WANDER` | strolls around | sees the player (closer than `sight_range`) → `CHASE` |
| `CHASE` | runs at the player | close enough (`attack_range`) → `ATTACK`; player gets away (farther than `sight_range × 1.5`) → `WANDER` |
| `ATTACK` | bites | player steps out of `attack_range` → `CHASE` |
| `FLEE` | runs away | from **any** state when health drops below 30% |

Two details make AI feel natural:

- **Lose sight further than you spot.** The wolf notices you at 200 pixels but only gives up at 300 (`× 1.5`). If both were 200, a player standing at exactly 200 would make the wolf flip between chasing and wandering every frame. This gap is called **hysteresis**.
- **Check the most important rule first.** Fleeing beats everything, so test it before the `match`.

Health below 30% means `health < max_health * 0.3`. With `max_health = 50` that's below 15.

## Your quest

Write `think(distance: float) -> void`, which picks the next `state` given the distance to the player, using the table. The check walks the wolf through a whole hunt.
