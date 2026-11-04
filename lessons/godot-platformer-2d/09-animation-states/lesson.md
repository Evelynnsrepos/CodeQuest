---
title: Choosing the animation
xp: 20
---
# Idle, run, jump, fall

A character usually has a few animations. In Godot an `AnimatedSprite2D` holds them (you add the frames in the **SpriteFrames** panel), and you switch with `play("run")`. Calling `play()` with the animation that's already playing does nothing, so it's fine to call it every frame.

Which one to play depends on what the body is doing:

| situation | animation |
| --- | --- |
| in the air, moving up (`velocity.y < 0`) | `"jump"` |
| in the air, moving down | `"fall"` |
| on the floor, moving sideways | `"run"` |
| on the floor, standing still | `"idle"` |

Sprites are usually drawn facing right. To face left, set `flip_h = true` on the sprite. Only change it while moving, so the character keeps facing the last way it walked when it stops.

```gdscript
func _physics_process(delta):
	# ...movement...
	move_and_slide()
	$AnimatedSprite2D.play(pick_animation(is_on_floor()))
	if velocity.x != 0:
		$AnimatedSprite2D.flip_h = velocity.x < 0
```

The floor check comes in as a parameter, `on_floor`, so the check can try every case without building a level.

## Your quest

1. Write `pick_animation(on_floor: bool) -> String` using the table.
2. Write `update_facing()`: if `velocity.x` isn't `0`, set `facing_left` to whether `velocity.x` is negative.
