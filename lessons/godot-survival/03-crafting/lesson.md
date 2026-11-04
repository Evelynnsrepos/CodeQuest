---
title: Crafting recipes
xp: 25
---
# 3 wood + 2 stone = axe

A crafting recipe is a list of ingredients and how many of each you need. A Dictionary inside a Dictionary is a natural fit:

```gdscript
var recipes := {
	"axe": {"wood": 3, "stone": 2},
	"campfire": {"wood": 5},
}
```

`recipes["axe"]` is `{"wood": 3, "stone": 2}`. Looping over a Dictionary gives you its keys:

```gdscript
for ingredient in recipes["axe"]:
	print(ingredient, " x", recipes["axe"][ingredient])   # wood x3, stone x2
```

Crafting has to be **all or nothing**. Check that *every* ingredient is there **before** taking anything out. Otherwise a player with 3 wood and 0 stone would lose their wood and get no axe!

The inventory here is a plain `{"item": count}` Dictionary (like Godot 1). The slot version from the last lesson works the same way, just with more bookkeeping.

## Your quest

1. `can_craft(thing: String) -> bool`: `true` if `thing` is a known recipe and `items` has enough of every ingredient.
2. `craft(thing: String) -> bool`: if you can craft it, remove the ingredients, add 1 `thing` to `items` and return `true`. Otherwise change nothing and return `false`.
