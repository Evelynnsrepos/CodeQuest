---
title: Coyote time and jump buffering
xp: 30
hint: On the floor, reset coyote_timer to coyote_time; in the air, count it down. Same idea for buffer_timer when jump is just pressed.
hint: Jump when buffer_timer > 0 and coyote_timer > 0, then set both to 0 so it can't jump twice.
---
# Forgiving jumps

> **Warm-up:** Have you ever pressed jump just after running off a ledge, and the game still let you?

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

<svg viewBox="0 0 480 210" width="100%" style="max-width:480px" role="img" aria-label="Coyote time lets you jump shortly after leaving a ledge; the jump buffer keeps a press made just before landing"><defs><marker id="ahct6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahcte5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker><marker id="ahct30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ahctd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker></defs><rect x="20.0" y="90.0" width="170.0" height="12.0" fill="currentColor" opacity="0.35" rx="2"/><rect x="300.0" y="150.0" width="160.0" height="12.0" fill="currentColor" opacity="0.35" rx="2"/><path d="M120,75 L190,75 Q215,78 235,100 Q260,140 300,138" stroke="#6c4cf5" stroke-width="2" fill="none" stroke-dasharray="5 4"/><rect x="110.0" y="60.0" width="14.0" height="30.0" fill="#6c4cf5" rx="2"/><rect x="190.0" y="60.0" width="70.0" height="30.0" fill="#30a46c" opacity="0.25" rx="2"/><text x="225.0" y="52.0" font-size="11" fill="#30a46c" text-anchor="middle">coyote time 0.1 s</text><text x="225.0" y="120.0" font-size="11" fill="#30a46c" text-anchor="middle">jump still works</text><rect x="255.0" y="120.0" width="45.0" height="30.0" fill="#d97706" opacity="0.25" rx="2"/><text x="277.0" y="175.0" font-size="11" fill="#d97706" text-anchor="middle">buffer 0.1 s</text><text x="277.0" y="190.0" font-size="11" fill="#d97706" text-anchor="middle">early press is kept</text><text x="105.0" y="125.0" font-size="11" fill="currentColor" text-anchor="middle">running off the ledge</text></svg>

## Your quest

Replace the plain `is_on_floor()` jump with coyote time and jump buffering, using `coyote_timer` and `buffer_timer`.

The check walks off a ledge and jumps 3 frames later, presses jump just before landing, and makes sure the player can't jump half a second after leaving the ground.

## Review

<details><summary>What is coyote time?</summary>A short grace time after leaving a ledge during which you can still jump.</details>
<details><summary>What is jump buffering?</summary>Remembering a jump press shortly before landing and jumping as soon as you land.</details>
