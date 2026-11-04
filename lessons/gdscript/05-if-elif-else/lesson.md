---
title: Making decisions
xp: 15
hint: Check the two special matchups first, then the same-element case, then return 1.0.
hint: and means both parts must be true: element == "fire" and enemy == "ice".
---
# if, elif, else

> **Warm-up:** In Pokémon-style games, why does fire beat ice?

Games make decisions all the time: *is the player dead? is the door locked?* `if` runs a block only when its condition is true. `elif` ("else if") tries another condition, and `else` catches everything left over.

```gdscript
func describe(health: int) -> String:
	if health <= 0:
		return "dead"
	elif health < 30:
		return "hurt"
	else:
		return "fine"
```

The conditions are checked **from top to bottom** and only the first true one runs. So the order matters: `health = 0` stops at the first line, even though `0 < 30` is also true.

Useful comparisons: `==` equal, `!=` not equal, `<` `<=` `>` `>=`. Combine them with `and`, `or` and `not`.

## Your quest

Write `damage_multiplier(element: String, enemy: String) -> float` for a little elemental system:

- `"fire"` against `"ice"` does double damage: `2.0`
- `"water"` against `"fire"` does double damage: `2.0`
- the same element against itself (`"fire"` vs `"fire"`) does half damage: `0.5`
- everything else: `1.0`

## Review

<details><summary>When does elif run?</summary>Only when every if and elif above it was false.</details>
<details><summary>Why check fire vs ice before element == enemy?</summary>Order matters: the first true branch wins, so the most specific cases go first.</details>
