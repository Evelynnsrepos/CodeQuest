---
title: Arrays and loops
xp: 20
---
# Collecting coins

An **Array** holds a list of values. A `for` loop goes through them one at a time.

```gdscript
var coins = [3, 7, 2]
for c in coins:
	print(c)
```

## Your quest

Write `count_big(coins: Array, at_least: int) -> int`. It returns how many values in `coins` are greater than or equal to `at_least`.

- `count_big([3, 7, 2, 10], 5)` returns `2`
- `count_big([], 1)` returns `0`
