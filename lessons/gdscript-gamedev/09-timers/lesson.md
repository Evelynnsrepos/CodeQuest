---
title: Timer nodes
xp: 20
hint: Timer.new(), set name and wait_time, then timer.timeout.connect(_on_spawn_timer_timeout).
hint: add_child(timer) and timer.start(). The timeout function only needs spawned += 1.
---
# Every two seconds, a zombie

> **Warm-up:** How would you make a new enemy appear every 2 seconds?

In the cooldown lesson you counted time down yourself. Godot's **Timer** node does that for you and emits its `timeout` signal when the time is up.

```gdscript
func _ready():
	var timer := Timer.new()
	timer.wait_time = 2.0     # seconds
	timer.one_shot = false    # false: start again by itself, forever
	timer.timeout.connect(_on_timer_timeout)
	add_child(timer)          # a Timer only ticks while it's in the scene tree
	timer.start()

func _on_timer_timeout():
	print("two more seconds passed")
```

In the editor you'd add the Timer as a child node, set **Wait Time** and **Autostart** in the Inspector, and connect `timeout` in the **Node → Signals** tab. Doing it in code shows exactly what those clicks do.

`one_shot = true` makes it fire just once, handy for "respawn in 3 seconds" or "invincible for 1 second".

For a quick one-time wait inside a function there's also a shortcut:

```gdscript
await get_tree().create_timer(1.5).timeout   # pause this function for 1.5 s
```

## Your quest

Make a wave spawner. In `_ready()`:

1. Create a `Timer` named `"SpawnTimer"` that repeats every `spawn_every` seconds (`0.2` here, so the check doesn't take long).
2. Connect its `timeout` to `_on_spawn_timer_timeout`.
3. Add it as a child and start it.

`_on_spawn_timer_timeout()` adds 1 to `spawned`. The check waits half a second, so about 2 enemies should have spawned.

## Review

<details><summary>Which signal does a Timer send when it runs out?</summary>timeout</details>
<details><summary>Does a Timer repeat by default?</summary>Yes, unless you set one_shot to true.</details>
