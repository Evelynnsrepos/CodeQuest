---
title: Functions
xp: 15
hint: health - damage can be negative. max(a, b) gives the bigger of two numbers.
hint: return max(health - damage, 0)
---
# Taking damage

> **Warm-up:** If a hit does more damage than you have health, what should your health be?

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

## Review

<details><summary>What does -&gt; int after a function mean?</summary>The function returns a whole number.</details>
<details><summary>Which function stops a number going below 0?</summary>max(value, 0): it returns whichever is bigger.</details>
