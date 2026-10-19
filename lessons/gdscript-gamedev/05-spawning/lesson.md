---
title: Spawning things
xp: 20
---
# A row of coins

Games create nodes while running: bullets, enemies, pickups. You make a node with `.new()` and put it in the scene with `add_child()`.

```gdscript
var enemy := Node2D.new()
enemy.name = "Enemy"
enemy.position = Vector2(100, 50)
add_child(enemy)
```

In a real project you'd usually design the coin as its own scene and spawn it with `preload("res://coin.tscn").instantiate()`. The idea is the same.

## Your quest

Write `spawn_coins(count: int, spacing: float)`. It adds `count` new `Node2D` children named `Coin0`, `Coin1`, ... in a row: coin `i` sits at `Vector2(i * spacing, 0)`.

`spawn_coins(3, 64)` makes coins at `(0, 0)`, `(64, 0)` and `(128, 0)`.
