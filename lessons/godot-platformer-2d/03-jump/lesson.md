---
title: Jumping to an exact height
xp: 30
hint: The formula is jump_velocity = -sqrt(2.0 * gravity * jump_height). The minus means up.
hint: if Input.is_action_just_pressed("ui_accept") and is_on_floor(): velocity.y = jump_velocity
---
# How high is a jump?

> **Warm-up:** Level designers say a ledge is 64 pixels high. What do you need to know to make the player reach it?

A jump is just a quick **upward speed**. Up is **negative y** in 2D, so a jump sets `velocity.y` to a negative number, and gravity (from lesson 1) slowly turns it around until the player falls again.

```gdscript
if Input.is_action_just_pressed("ui_accept") and is_on_floor():
	velocity.y = jump_velocity
```

`is_action_just_pressed` is true only on the **one frame** the key goes down, so holding the key doesn't jump again and again. The `is_on_floor()` part stops jumping in mid-air.

## Picking the jump speed from the height you want

Level designers think in **heights** ("the player can reach a 64-pixel ledge"), not in speeds. Physics gives a formula that turns one into the other. Let's build it step by step.

**Step 1.** Going up, gravity removes `g` from your speed every second. You start at speed `v` and stop at the top, so the trip up takes

```
time = v ÷ g
```

**Step 2.** Your speed drops evenly from `v` to `0`, so your **average** speed on the way up is halfway: `v ÷ 2`.

**Step 3.** Distance is average speed times time:

```
height = (v ÷ 2) × (v ÷ g) = v² ÷ (2 × g)
```

**Step 4.** We know the height and want `v`, so turn the formula around. Multiply both sides by `2 × g`, then take the square root (`√`, "which number times itself gives this?"):

```
v² = 2 × g × height
v  = √(2 × g × height)
```

Let's try it with `g = 980` and `height = 64`:

```
2 × 980 × 64 = 125440
√125440 ≈ 354.2
```

So the player needs `354.2` px/s upwards, which is `velocity.y = -354.2` (negative = up). In GDScript, `sqrt(x)` is the square root:

```gdscript
var jump_velocity := -sqrt(2.0 * gravity * jump_height)
```

Now you can change `jump_height` and the speed follows. That's how designers tune games.

<svg viewBox="0 0 420 240" width="100%" style="max-width:420px" role="img" aria-label="A jump arc: the player starts with an upward speed, gravity slows it, the top is 64 pixels above the floor"><defs><marker id="ahjp6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahjpe5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker><marker id="ahjp30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ahjpd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker></defs><rect x="20.0" y="200.0" width="380.0" height="12.0" fill="currentColor" opacity="0.35" rx="2"/><text x="30.0" y="228.0" font-size="11" fill="currentColor" text-anchor="start">floor</text><path d="M40.0,185.0 L47.5,172.3 L55.0,160.3 L62.5,148.9 L70.0,138.2 L77.5,128.1 L85.0,118.7 L92.5,109.9 L100.0,101.8 L107.5,94.3 L115.0,87.5 L122.5,81.3 L130.0,75.8 L137.5,70.9 L145.0,66.7 L152.5,63.1 L160.0,60.2 L167.5,57.9 L175.0,56.3 L182.5,55.3 L190.0,55.0 L197.5,55.3 L205.0,56.3 L212.5,57.9 L220.0,60.2 L227.5,63.1 L235.0,66.7 L242.5,70.9 L250.0,75.8 L257.5,81.3 L265.0,87.5 L272.5,94.3 L280.0,101.8 L287.5,109.9 L295.0,118.7 L302.5,128.1 L310.0,138.2 L317.5,148.9 L325.0,160.3 L332.5,172.3 L340.0,185.0" stroke="#6c4cf5" stroke-width="2.5" fill="none" stroke-dasharray="5 4"/><rect x="30.0" y="170.0" width="20.0" height="30.0" fill="#6c4cf5" rx="2"/><rect x="180.0" y="40.0" width="20.0" height="30.0" fill="#6c4cf5" opacity="0.6" rx="2"/><rect x="330.0" y="170.0" width="20.0" height="30.0" fill="#6c4cf5" opacity="0.35" rx="2"/><line x1="40.0" y1="166.0" x2="40.0" y2="100.0" stroke="#e5484d" stroke-width="2.5" marker-end="url(#ahjpe5484d)"/><text x="20.0" y="34.0" font-size="12" fill="#e5484d" text-anchor="start">jump: velocity.y = −354</text><line x1="240.0" y1="60.0" x2="240.0" y2="90.0" stroke="#d97706" stroke-width="2" marker-end="url(#ahjpd97706)"/><line x1="270.0" y1="75.0" x2="270.0" y2="105.0" stroke="#d97706" stroke-width="2" marker-end="url(#ahjpd97706)"/><text x="285.0" y="80.0" font-size="11" fill="#d97706" text-anchor="start">gravity pulls 980 px/s down every second</text><line x1="215.0" y1="55.0" x2="215.0" y2="185.0" stroke="#30a46c" stroke-width="1.5" stroke-dasharray="5 4"/><text x="222.0" y="125.0" font-size="12" fill="#30a46c" text-anchor="start" font-weight="bold">64 px</text><text x="190.0" y="20.0" font-size="11" fill="currentColor" text-anchor="middle">top: speed is 0 here</text></svg>

## Your quest

1. Work out `jump_velocity` from `jump_height` and `gravity` with the formula (don't forget the minus sign).
2. In `_physics_process`, jump when `ui_accept` (Space or Enter) is just pressed **and** the player is on the floor.

The check measures your jump: its top should be about 64 pixels above the floor, and pressing jump in mid-air must do nothing.

## Review

<details><summary>Why is jump_velocity negative?</summary>Up is negative y in 2D.</details>
<details><summary>What speed reaches a 64-pixel jump with gravity 980?</summary>About 354, from the square root of 2 x 980 x 64.</details>
<details><summary>Why is_action_just_pressed and not is_action_pressed?</summary>Just pressed is true for one frame only, so holding the key doesn't keep jumping.</details>
