---
title: Loops
xp: 20
---
# Counting the loot

A **list** holds many values. A `for` loop visits each one in turn.

```python
coins = [3, 7, 2]
for c in coins:
    print(c)
```

## Your quest

Write `total_loot(chests)` that takes a list of numbers (the gold in each chest) and returns the total. Use a `for` loop instead of `sum()` this time.

- `total_loot([3, 7, 2])` returns `12`
- `total_loot([])` returns `0`
