---
title: Player input
xp: 20
---
# Arrow keys

Godot has built-in **input actions** such as `ui_left`, `ui_right`, `ui_up` and `ui_down` (the arrow keys). In your own projects you can add more in **Project Settings → Input Map**, like `jump` or `move_left`.

`Input.get_vector()` turns four actions into one direction:

```gdscript
var direction := Input.get_vector("ui_left", "ui_right", "ui_up", "ui_down")
```

It gives `Vector2(1, 0)` when holding right, `Vector2(0, -1)` when holding up (y points **down** in 2D), and a diagonal of length 1 when holding two keys, so diagonal movement isn't faster.

## Your quest

Move the player at `speed` pixels per second in the direction of the arrow keys.

- Holding right for half a second moves the player `150` pixels right.
- Holding up and left moves diagonally, still `150` pixels in total.
