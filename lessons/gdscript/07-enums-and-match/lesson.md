---
title: Enums and match
xp: 20
hint: Check the smallest distance first: if distance <= 30 attack, elif distance <= 200 chase, else idle.
hint: In describe(), each match branch looks like State.ATTACK: and then return "attack" on the next line.
---
# What is the enemy doing?

> **Warm-up:** Name three things an enemy in a game might be doing.

An enemy is usually in one **state** at a time: idle, chasing, attacking. You could store that as a String, but a typo like `"chasng"` would never be caught. An **enum** gives each state a name that Godot checks for you:

```gdscript
enum State { IDLE, CHASE, ATTACK }

var state := State.IDLE
```

Behind the scenes `IDLE` is `0`, `CHASE` is `1` and `ATTACK` is `2`, but you only ever use the names.

`match` is a tidy way to do something different for each value, instead of a long `if/elif` chain:

```gdscript
match state:
	State.IDLE:
		print("standing around")
	State.CHASE, State.ATTACK:   # one branch for two values
		print("busy!")
	_:                          # _ means "anything else"
		print("???")
```

This pattern is called a **state machine**, and nearly every game uses it: for the player (standing, running, jumping), enemies, menus and even the whole game (playing, paused, game over).

## Your quest

Write `next_state(distance: float) -> void` for an enemy with `var state := State.IDLE`. It changes `state` based on how far away the player is:

- `distance` up to `30` (including 30): `State.ATTACK`
- up to `200` (including 200): `State.CHASE`
- farther: `State.IDLE`

Then write `describe() -> String` with `match`: it returns `"idle"`, `"chase"` or `"attack"` for the current state.

## Review

<details><summary>Why use an enum instead of strings like "chase"?</summary>Godot checks the names for you, so a typo is an error instead of a silent bug.</details>
<details><summary>What does _ mean in a match?</summary>Anything else: the branch used when no other value matched.</details>
