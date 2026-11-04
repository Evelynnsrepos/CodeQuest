---
title: Dictionaries
xp: 20
hint: bag.get(item, 0) gives the count, or 0 if the item isn't in the bag yet.
hint: In remove_item, check bag.get(item, 0) < amount first and return false before changing anything.
---
# A bag of loot

> **Warm-up:** How would a game remember that you carry 3 wood and 2 stone?

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

## Review

<details><summary>What does bag.get("wood", 0) return if there is no wood?</summary>0, the default you passed.</details>
<details><summary>How do you remove a key from a dictionary?</summary>bag.erase(key)</details>
