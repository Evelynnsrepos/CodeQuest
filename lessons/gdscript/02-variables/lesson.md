---
title: Variables and types
xp: 10
---
# Your player's stats

Variables are declared with `var`. Variables declared at the top of a script (outside any function) belong to the whole script, like a node's properties in Godot.

```gdscript
var speed := 200      # := lets Godot work out the type (int)
var player_name: String = "Ada"
```

## Your quest

The script has `var health := 100`. Inside `run()`:

1. Subtract 25 from `health` (a trap!).
2. Print `health`.

It should print `75`, and `health` should be `75` afterwards.
