---
title: Short hops and big jumps
xp: 20
---
# Hold to jump higher

In most good platformers, **tapping** jump makes a short hop and **holding** it makes a full jump. That gives the player fine control. The trick is simple: if the player lets go of the button while still going **up**, cut the upward speed.

```gdscript
if Input.is_action_just_released("ui_accept") and velocity.y < 0:
	velocity.y *= 0.5
```

`velocity.y < 0` means "moving up" (remember, up is negative). `*= 0.5` halves the speed. Since the height grows with the **square** of the speed (`v²` in the last lesson), half the speed leaves only a quarter of the remaining rise: `0.5 × 0.5 = 0.25`.

`jump_cut` is how much speed to keep: `0.5` keeps half. Try `0.3` for a snappier hop.

## Your quest

The jump is done. Add the jump cut: when `ui_accept` is **just released** while moving up, multiply `velocity.y` by `jump_cut`.

The check taps jump quickly once and holds it once. The tap should be clearly lower than the full jump.
