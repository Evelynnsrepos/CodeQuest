---
title: Functions
xp: 15
---
# Taking damage

Functions are declared with `func`. You can add **type hints** to parameters and the return value, which helps Godot catch mistakes early.

```gdscript
func heal(health: int, amount: int) -> int:
	return health + amount
```

`max(a, b)` returns the bigger of two numbers.

## Your quest

Write `take_damage(health: int, damage: int) -> int`. It returns the health left after the hit, but never goes below `0`.

- `take_damage(100, 30)` returns `70`
- `take_damage(10, 50)` returns `0`
