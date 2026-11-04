---
title: The basis, or which way is forward
xp: 30
hint: Turn with rotation.y += turn * turn_speed * delta.
hint: var direction := transform.basis * Vector3(0, 0, forward) turns local forward into world space.
---
# Walking where you face

> **Warm-up:** You turn your character to the left. Which way is forward now?

Last lesson, "up arrow" always moved towards -z, wherever the player was looking. In most 3D games, forward should mean **the way the character faces**. For that we need the **basis**.

## Three arrows glued to the object

Every 3D node carries three arrows that turn with it. Together they're called its **basis** (`transform.basis`):

- `basis.x`: the node's own **right**
- `basis.y`: its own **up**
- `basis.z`: its own **back** (so `-basis.z` is its **forward**)

When the node hasn't turned, they're just the world axes: right = (1, 0, 0), up = (0, 1, 0), back = (0, 0, 1).

Now turn the node left by 90° (`rotation.y = PI / 2`; a positive turn around y is to the **left**, seen from above). Its arrows turn with it:

- its right now points where the world's forward was: `basis.x = (0, 0, -1)`
- its back now points the world's right: `basis.z = (1, 0, 0)`, so its forward is `(-1, 0, 0)`, the world's left ✔ (it turned left)

## Turning a local direction into a world direction

Our input direction is **local**: "(0, 0, -1)" means "my forward". Multiplying by the basis turns it into a **world** direction:

```gdscript
var direction := transform.basis * Vector3(input.x, 0, input.y)
```

Behind the `*`, Godot does this:

```
basis * (a, b, c) = a × basis.x + b × basis.y + c × basis.z
```

In words: "go `a` steps along my right arrow, `b` along my up arrow and `c` along my back arrow". With the node turned left 90° and the up arrow held, the input is (0, 0, -1):

```
0 × basis.x + 0 × basis.y + (-1) × basis.z
= -1 × (1, 0, 0)
= (-1, 0, 0)        → the world's left, which is where the player faces ✔
```

That one line is how nearly every 3D character controller moves. Godot's CharacterBody3D template uses it too, with `.normalized()` on the end.

## Your quest

Turn the player with the left and right arrows, and walk forward and back with up and down, in the direction it faces ("tank controls", like old survival horror games):

1. `rotation.y += turn * turn_speed * delta`, where `turn` is `Input.get_axis("ui_right", "ui_left")` (right first, so the right arrow gives -1, a turn to the right).
2. `var forward := Input.get_axis("ui_up", "ui_down")` gives -1 for up.
3. Turn `Vector3(0, 0, forward)` into a world direction with the basis and use it for `velocity.x` and `velocity.z` at `speed`.

## Review

<details><summary>What is the basis?</summary>The three arrows (x, y, z) that say which way the node's right, up and back point in the world.</details>
<details><summary>Which direction is forward for a Godot 3D node?</summary>-z.</details>
