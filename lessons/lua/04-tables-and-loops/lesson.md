---
title: Tables and loops
xp: 20
---
# The inventory

A **table** is Lua's one data structure. Used as a list, it holds values in order, and **counting starts at 1**, not 0.

```lua
local items = {"sword", "shield", "potion"}
print(items[1])   -- sword
print(#items)     -- 3, the length

for i, item in ipairs(items) do
  print(i, item)
end
```

## Your quest

Write `count_potions(items)` that returns how many entries in `items` are exactly `"potion"`.

- `count_potions({"potion", "sword", "potion"})` returns `2`
- `count_potions({})` returns `0`
