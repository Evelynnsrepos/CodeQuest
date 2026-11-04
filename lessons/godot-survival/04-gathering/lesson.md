---
title: Gathering resources
xp: 25
---
# Chop chop

Trees, rocks and bushes are **resource nodes**: hit them a few times and they drop items, then disappear (and maybe grow back later).

The tree doesn't know about your inventory. It just announces what dropped with a signal, and whoever is listening (the player, or a pickup spawner) handles it. You've seen this decoupling with health and the HUD.

Tools matter in survival games: an axe chops faster than bare hands. A Dictionary maps each tool to its power, and `get(tool, 1)` means "anything unknown counts as 1, like hands".

```gdscript
var tool_power := {"hand": 1, "stone_axe": 2, "iron_axe": 4}
```

`maxi(hits_left - power, 0)` keeps the hits from going below zero.

## Your quest

The tree starts with `hits_left := 6`. Write `hit(tool: String)`:

1. Ignore the hit if the tree is already used up (`hits_left` is `0`).
2. Lower `hits_left` by the tool's power (unknown tools count as `1`), not below `0`.
3. Emit `dropped("wood", amount)` with the same amount as the power used. Use `mini` so the drop is at most what was left: an iron axe (4) hitting a tree with 2 hits left drops 2.
4. When `hits_left` reaches `0`, emit `depleted` and `queue_free()` the tree.
