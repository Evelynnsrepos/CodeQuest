---
title: Enemy chase
xp: 25
hint: position.distance_to(target) <= sight_range
hint: position.move_toward(target, speed * delta) moves at most that far and never overshoots.
---
# It's coming for you

> **Warm-up:** When should a guard in a stealth game start chasing you?

Simple enemy AI is often just two questions: *can I see the player?* and *which way do I move?* `Vector2` has helpers for both:

```gdscript
position.distance_to(target)               # how far away, in pixels
position.move_toward(target, max_step)     # step towards target without overshooting
```

## Your quest

The enemy has `speed := 80.0` and `sight_range := 200.0`. Write:

1. `can_see(target: Vector2) -> bool`: `true` when the target is within `sight_range` (exactly 200 away counts).
2. `chase(target: Vector2, delta: float)`: if the enemy can see the target, move towards it by at most `speed * delta` pixels. If not, stay still.

## Review

<details><summary>What does move_toward do that plain adding doesn't?</summary>It stops exactly at the target instead of overshooting.</details>
<details><summary>Does a target exactly 200 away count as seen with sight_range 200?</summary>Yes, because the check is &lt;=.</details>
