---
title: Making decisions
xp: 15
---
# if, elif, else

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
