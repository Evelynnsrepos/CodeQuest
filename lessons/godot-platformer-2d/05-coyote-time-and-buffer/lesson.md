---
title: Coyote time and jump buffering
xp: 30
---
# Forgiving jumps

Two hidden tricks make a platformer feel **fair**. Players almost never notice them, but they notice when they're missing.

**Coyote time**: like the cartoon coyote who runs off a cliff and only falls when he looks down, the player can still jump for a few frames *after* walking off a ledge. Without it, pressing jump a hair too late does nothing and feels broken.

**Jump buffering**: if the player presses jump a few frames *before* landing, remember it and jump the moment they touch the ground.

Both are small countdown timers, like your cooldown from Basics 2:

```gdscript
# coyote: full while on the floor, counts down in the air
if is_on_floor():
	coyote_timer = coyote_time
else:
	coyote_timer -= delta

# buffer: full when jump is pressed, counts down after
if Input.is_action_just_pressed("ui_accept"):
	buffer_timer = buffer_time
else:
	buffer_timer -= delta
```

Then the jump happens when **both** timers are still above zero: "jump was pressed recently" and "was on the floor recently". After jumping, set both to `0`, so one press can't jump twice.

`0.1` seconds is 6 frames. It sounds tiny, but it's the difference between "I pressed it!" and a happy player.

## Your quest

Replace the plain `is_on_floor()` jump with coyote time and jump buffering, using `coyote_timer` and `buffer_timer`.

The check walks off a ledge and jumps 3 frames later, presses jump just before landing, and makes sure the player can't jump half a second after leaving the ground.
