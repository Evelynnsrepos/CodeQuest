---
title: Variables and types
xp: 10
hint: health -= 25 means health = health - 25.
hint: Print health after you change it, not before.
---
# Your player's stats

> **Warm-up:** Your hero has 100 health and gets hit for 25. How would you write that down?

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

## Review

<details><summary>What does := do in var health := 100?</summary>It creates the variable and lets Godot work out its type (int) from the value.</details>
<details><summary>What is the short way to write health = health - 25?</summary>health -= 25</details>
