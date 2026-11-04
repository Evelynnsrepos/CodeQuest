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
