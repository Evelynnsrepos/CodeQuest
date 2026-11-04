---
title: Spawning things
xp: 20
hint: for i in count: makes i go 0, 1, 2...
hint: Inside the loop: Node2D.new(), set name to "Coin%d" % i, set position to Vector2(i * spacing, 0), then add_child(coin).
---
# A row of coins

> **Warm-up:** How would you place 3 coins in a row, 64 pixels apart?

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

## Review

<details><summary>What does Node2D.new() do?</summary>Creates a new node in code; it isn't in the scene until you add_child it.</details>
<details><summary>What does "Coin%d" % 2 give?</summary>"Coin2"</details>
