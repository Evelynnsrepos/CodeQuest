---
title: Vector math, step by step
xp: 25
hint: The arrow from A to B is B - A. Here A is the enemy and B is the player: position - enemy_position.
hint: (position - enemy_position).normalized() * strength, added to position.
---
# Arrows that point somewhere

> **Warm-up:** You stand at (100, 0) and an enemy at (0, 0) hits you. Which way should you fly?

You've used `Vector2` for positions. A vector is just **two numbers, x and y**. You can read it in two ways:

- as a **place**: `Vector2(3, 4)` is "3 right, 4 down from the top-left corner"
- as an **arrow** (a step): `Vector2(3, 4)` is "move 3 right and 4 down"

Every shooter, platformer and survival game uses a handful of tricks with these arrows. Let's take them one at a time.

## 1. The arrow from A to B: subtract

To get from `A` to `B`, take **B minus A**. Subtract x from x and y from y:

```
A = (1, 2)      B = (4, 6)
B - A = (4 - 1, 6 - 2) = (3, 4)
```

So the arrow from A to B is "3 right, 4 down". Check: start at A = (1, 2), add (3, 4), and you land on (4, 6), which is B. ✔

The order matters: `A - B = (-3, -4)` is the arrow pointing the **other** way, from B back to A.

## 2. How long is the arrow: `length()`

The arrow (3, 4) goes 3 across and 4 down. How long is it in a straight line? The x and y parts form the two short sides of a right-angled triangle, and the arrow is the long side. Pythagoras' rule says:

```
length² = x² + y²
```

`x²` ("x squared") means x times x. Step by step:

```
x² = 3 × 3 = 9
y² = 4 × 4 = 16
9 + 16 = 25
length = √25 = 5     (√ means "which number times itself gives this?" 5 × 5 = 25)
```

Godot does this for you: `Vector2(3, 4).length()` is `5`. And `A.distance_to(B)` is the same as `(B - A).length()`.

## 3. Only the direction: `normalized()`

Often you want the **direction** but not the length, for example "move towards the player at my own speed". `normalized()` shrinks (or stretches) an arrow to length **1** while keeping where it points. It divides both parts by the length:

```
(3, 4) has length 5
(3 ÷ 5, 4 ÷ 5) = (0.6, 0.8)
```

Check: 0.6² + 0.8² = 0.36 + 0.64 = 1, so the new length is √1 = 1. ✔

A length-1 vector is called a **unit vector**. Multiply it by a speed and you get "this direction, that fast": `Vector2(0.6, 0.8) * 100 = (60, 80)`, which is exactly 100 pixels long.

`A.direction_to(B)` is a shortcut for `(B - A).normalized()`.

<svg viewBox="0 0 360 310" width="100%" style="max-width:360px" role="img" aria-label="The arrow from A at (1, 2) to B at (4, 6) is B minus A, which is (3, 4) and 5 long"><defs><marker id="ahvm6c4cf5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#6c4cf5"/></marker><marker id="ahvme5484d" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#e5484d"/></marker><marker id="ahvm30a46c" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#30a46c"/></marker><marker id="ahvmd97706" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="7" markerHeight="7" orient="auto-start-reverse"><path d="M0,0 L10,5 L0,10 z" fill="#d97706"/></marker></defs><line x1="40.0" y1="20.0" x2="320.0" y2="20.0" stroke="currentColor" stroke-width="1.5" opacity="0.45"/><line x1="40.0" y1="20.0" x2="40.0" y2="300.0" stroke="currentColor" stroke-width="1.5" opacity="0.45"/><text x="326.0" y="24.0" font-size="12" fill="currentColor" text-anchor="start">x</text><text x="48.0" y="300.0" font-size="12" fill="currentColor" text-anchor="start">y (down)</text><line x1="80.0" y1="100.0" x2="200.0" y2="100.0" stroke="#d97706" stroke-width="1.5" stroke-dasharray="5 4"/><line x1="200.0" y1="100.0" x2="200.0" y2="260.0" stroke="#d97706" stroke-width="1.5" stroke-dasharray="5 4"/><text x="140.0" y="94.0" font-size="12" fill="#d97706" text-anchor="middle">x: 4 − 1 = 3</text><text x="208.0" y="180.0" font-size="12" fill="#d97706" text-anchor="start">y: 6 − 2 = 4</text><line x1="80.0" y1="100.0" x2="197.0" y2="256.0" stroke="#6c4cf5" stroke-width="2.5" marker-end="url(#ahvm6c4cf5)"/><text x="122.0" y="196.0" font-size="12" fill="#6c4cf5" text-anchor="end" font-weight="bold">B − A = (3, 4)</text><text x="122.0" y="212.0" font-size="12" fill="#6c4cf5" text-anchor="end">length 5</text><circle cx="80.0" cy="100.0" r="4.5" fill="#e5484d"/><text x="72.0" y="94.0" font-size="12" fill="#e5484d" text-anchor="end">A (1, 2)</text><circle cx="200.0" cy="260.0" r="4.5" fill="#30a46c"/><text x="208.0" y="264.0" font-size="12" fill="#30a46c" text-anchor="start">B (4, 6)</text></svg>

## Your quest: knockback

When an enemy hits the player, push the player **away from the enemy**.

Write `knockback(enemy_position: Vector2, strength: float)`:

1. Work out the arrow **from the enemy to the player** (which one do you subtract?).
2. Normalize it so it has length 1.
3. Move the player's `position` by that direction times `strength`.

Example: the player at `(100, 0)`, the enemy at `(0, 0)`, strength `50`. The arrow from enemy to player is `(100, 0)`, normalized `(1, 0)`, so the player ends at `(150, 0)`.

## Review

<details><summary>What is the arrow from A to B?</summary>B - A.</details>
<details><summary>What does normalized() do?</summary>Keeps the direction but makes the length 1.</details>
<details><summary>How long is Vector2(3, 4)?</summary>5, because 3x3 + 4x4 = 25 and the square root of 25 is 5.</details>
