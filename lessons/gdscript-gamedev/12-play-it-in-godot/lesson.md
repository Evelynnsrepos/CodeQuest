---
title: Play it in Godot
xp: 30
hint: Vector2 has a clamp(min, max) function that keeps both x and y between two corners.
hint: After moving, write position = position.clamp(play_area.position, play_area.end).
---
# Your first playable scene

> **Warm-up:** In a game, what stops you walking off the edge of the screen?

> ✅ Tick the boxes as you go. Your ticks are saved on this device, so you can stop and come back any time.

Until now your code ran inside CodeQuest. Time to see it in the real Godot editor and move something with your own keys. This takes about 10 minutes, and you only need what you learned in this course.

## 1. Make a project

- [ ] Open Godot 4 and click **Create** in the Project Manager. Name it `first-game`, keep **Forward+** (or **Compatibility** on an older PC), and create it.
- [ ] Click **2D Scene** in the Scene dock. You get a `Node2D` called `Node2D`. Rename it to `Player` (double-click the name).
- [ ] Drag `icon.svg` from the **FileSystem** dock onto the `Player` node. That adds a `Sprite2D` child: the Godot robot is your player.
- [ ] Press **Ctrl+S** and save the scene as `player.tscn`.

## 2. Give it a script

- [ ] Select `Player`, click the **scroll with a +** button above the scene tree, and press **Create**.
- [ ] Paste in the code from this lesson's editor (once your quest passes).
- [ ] Press **F6** (Run Current Scene). Move the robot with the arrow keys!

The window is 1152 × 648 pixels by default (**Project → Project Settings → Display → Window**). Without a limit, the robot happily walks off the screen and is gone.

## Your quest: stay on screen

`play_area` is a `Rect2`, a rectangle with a `position` (its top-left corner) and an `end` (its bottom-right corner):

```
play_area = Rect2(0, 0, 1152, 648)
play_area.position = (0, 0)        top-left
play_area.end      = (1152, 648)   bottom-right
```

To keep the player inside, **clamp** the position after moving: any x below 0 becomes 0, any x above 1152 becomes 1152, and the same for y. `Vector2.clamp(min, max)` does both at once:

```gdscript
Vector2(-20, 700).clamp(Vector2(0, 0), Vector2(1152, 648))   # → (0, 648)
```

1. Move the player with the arrow keys at `speed`, like lesson 2.
2. Then clamp `position` to `play_area`.

The check holds the arrow keys towards each edge and makes sure the player stops there.

**Tick when done:**

- [ ] The quest passed and you pasted the code into Godot
- [ ] You pressed F6 and the robot stops at the window edges

## Review

<details><summary>What does Vector2.clamp(min, max) do?</summary>Keeps x between min.x and max.x and y between min.y and max.y.</details>
<details><summary>Which key runs only the scene you have open?</summary>F6. F5 runs the project's main scene.</details>
<details><summary>What are a Rect2's position and end?</summary>Its top-left corner and its bottom-right corner.</details>
