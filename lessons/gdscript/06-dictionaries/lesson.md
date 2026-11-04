---
title: Dictionaries
xp: 20
---
# A bag of loot

An **Array** finds things by position (`items[0]`). A **Dictionary** finds things by a name, called a **key**. It's perfect for an inventory: the key is the item name and the **value** is how many you have.

```gdscript
var bag := {"wood": 3, "stone": 1}

print(bag["wood"])            # 3
bag["wood"] += 2              # now 5
bag["rope"] = 1               # adds a new key
print(bag.get("iron", 0))     # 0: get() gives a default when the key is missing
print(bag.has("stone"))       # true
bag.erase("stone")            # removes the key
```

Reading `bag["iron"]` when there is no `"iron"` key is an **error**, so use `get(key, default)` or `has(key)` when you're not sure.

## Your quest

The script has `var bag := {}`. Write two functions:

1. `add_item(item: String, amount: int)` adds `amount` of `item` to the bag (creating the key if it's new).
2. `remove_item(item: String, amount: int) -> bool`: if the bag has at least `amount` of `item`, take them out and return `true`. If not, change nothing and return `false`. When an item's count reaches `0`, erase its key so the bag doesn't fill up with zeros.
