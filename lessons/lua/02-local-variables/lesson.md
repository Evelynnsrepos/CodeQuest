---
title: Local variables
xp: 10
---
# Keeping score

Create variables with `local`. Without `local`, a variable is **global** and visible everywhere, which causes bugs in bigger games, so get used to writing `local`.

```lua
local score = 0
score = score + 10   -- Lua has no += shortcut
print(score)         -- 10
```

## Your quest

Your hero has `local health = 100`. A slime hits for 25.

1. Subtract 25 from `health`.
2. Print `health`.

The program should print `75`.
