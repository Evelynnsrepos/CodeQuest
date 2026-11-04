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

<svg viewBox="0 0 380 245" width="100%" style="max-width:380px" role="img" aria-label="Seen from above, a body turned 30 degrees: its own forward and right arrows, the basis, point away from the world axes"><defs><marker id="ahbs6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahbse5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker><marker id="ahbs30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ahbsd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker></defs><line x1="170.0" y1="130.0" x2="170.0" y2="25.0" stroke="currentColor" stroke-width="1" stroke-dasharray="5 4" opacity="0.5"/><text x="170.0" y="18.0" font-size="11" fill="currentColor" text-anchor="middle">world forward (−z)</text><line x1="170.0" y1="130.0" x2="300.0" y2="130.0" stroke="currentColor" stroke-width="1" stroke-dasharray="5 4" opacity="0.5"/><text x="304.0" y="134.0" font-size="11" fill="currentColor" text-anchor="start">world x</text><rect x="156.0" y="116.0" width="28.0" height="28.0" fill="#6c4cf5" opacity="0.5" rx="2"/><line x1="170.0" y1="130.0" x2="125.0" y2="52.1" stroke="#e5484d" stroke-width="2.5" marker-end="url(#ahbse5484d)"/><text x="118.0" y="40.9" font-size="11" fill="#e5484d" text-anchor="end">its forward: −basis.z</text><line x1="170.0" y1="130.0" x2="239.3" y2="90.0" stroke="#30a46c" stroke-width="2.5" marker-end="url(#ahbs30a46c)"/><text x="246.7" y="82.0" font-size="11" fill="#30a46c" text-anchor="start">its right: basis.x</text><path d="M170,80 A50,50 0 0,0 145.0,86.7" stroke="#d97706" stroke-width="2" fill="none"/><text x="136.0" y="76.0" font-size="11" fill="#d97706" text-anchor="end">turned 30°</text><text x="170.0" y="235.0" font-size="11" fill="currentColor" text-anchor="middle">seen from above: basis × Vector3(0, 0, −1) is the way it faces</text></svg>

## Your quest

Turn the player with the left and right arrows, and walk forward and back with up and down, in the direction it faces ("tank controls", like old survival horror games):

1. `rotation.y += turn * turn_speed * delta`, where `turn` is `Input.get_axis("ui_right", "ui_left")` (right first, so the right arrow gives -1, a turn to the right).
2. `var forward := Input.get_axis("ui_up", "ui_down")` gives -1 for up.
3. Turn `Vector3(0, 0, forward)` into a world direction with the basis and use it for `velocity.x` and `velocity.z` at `speed`.

## Review

<details><summary>What is the basis?</summary>The three arrows (x, y, z) that say which way the node's right, up and back point in the world.</details>
<details><summary>Which direction is forward for a Godot 3D node?</summary>-z.</details>
