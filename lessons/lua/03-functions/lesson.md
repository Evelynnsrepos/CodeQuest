---
title: Functions
xp: 15
---
# Coins for every level

Functions start with `function` and finish with `end`. Use `return` to give back a result.

```lua
local function double(n)
  return n * 2
end

print(double(4))  -- 8
```

Lua uses `end` to close blocks instead of indentation, but indenting still makes code easier to read.

## Your quest

Write a function `coins_for(level)` that returns the level times 50.

- `coins_for(1)` returns `50`
- `coins_for(4)` returns `200`

Keep it global (no `local` before `function`) so the checker can find it.
