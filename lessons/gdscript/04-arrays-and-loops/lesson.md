---
title: Arrays and loops
xp: 20
hint: Start a counter at 0 before the loop.
hint: for c in coins: and inside it, if c >= at_least: count += 1. Return count after the loop.
---
# Collecting coins

> **Warm-up:** You have a bag of coins worth 3, 7, 2 and 10. How do you count the ones worth 5 or more?

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

## Review

<details><summary>What does for c in coins do?</summary>It runs the loop body once for every value in coins, with c set to that value.</details>
<details><summary>Where must return count go so every coin is counted?</summary>After the loop, not inside it.</details>
