---
title: Cooldowns
xp: 20
---
# No spamming the fire button

Most games stop you from shooting every frame. A common trick is a **cooldown timer**: a number that counts down in `_process` and blocks the action while it's above zero.

```gdscript
var _cooldown := 0.0   # a leading _ means "private to this script"

func _process(delta):
	_cooldown = max(_cooldown - delta, 0.0)
```

Godot also has a `Timer` node that does this for you, but writing it yourself shows how it works.

## Your quest

Write `try_shoot() -> bool`:

- If the cooldown is still running, return `false`.
- Otherwise start the cooldown at `cooldown_time` and return `true`.

Also count the cooldown down in `_process(delta)`. With `cooldown_time = 0.5`, shooting again after 0.3 s fails, after 0.6 s works.
