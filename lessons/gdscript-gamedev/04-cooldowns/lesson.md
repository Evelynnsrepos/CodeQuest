---
title: Cooldowns
xp: 20
hint: In _process, count _cooldown down: _cooldown = max(_cooldown - delta, 0.0).
hint: try_shoot: if _cooldown > 0.0 return false, otherwise set _cooldown = cooldown_time and return true.
---
# No spamming the fire button

> **Warm-up:** Why can't you fire a gun 1,000 times a second in most games?

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

## Review

<details><summary>What does a cooldown variable hold?</summary>How many seconds are left until you can act again.</details>
<details><summary>Where do you count it down?</summary>In _process(delta), by delta each frame.</details>
