---
title: Enemy chase
xp: 25
---
# It's coming for you

Simple enemy AI is often just two questions: *can I see the player?* and *which way do I move?* `Vector2` has helpers for both:

```gdscript
position.distance_to(target)               # how far away, in pixels
position.move_toward(target, max_step)     # step towards target without overshooting
```

## Your quest

The enemy has `speed := 80.0` and `sight_range := 200.0`. Write:

1. `can_see(target: Vector2) -> bool`: `true` when the target is within `sight_range` (exactly 200 away counts).
2. `chase(target: Vector2, delta: float)`: if the enemy can see the target, move towards it by at most `speed * delta` pixels. If not, stay still.
