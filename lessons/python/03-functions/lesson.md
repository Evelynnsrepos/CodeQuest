---
title: Functions
xp: 15
---
# Reusable magic

A **function** is a named block of code you can use again and again. It can take inputs (parameters) and give back a result with `return`.

```python
def double(n):
    return n * 2

print(double(4))  # 8
```

The body of a function is **indented** by four spaces.

## Your quest

Write a function `xp_needed(level)` that returns how much XP a level needs: the level number times 100.

- `xp_needed(1)` returns `100`
- `xp_needed(5)` returns `500`
