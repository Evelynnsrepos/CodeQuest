---
title: The third dimension
xp: 25
---
# x, y and z

In 3D, positions are `Vector3`: three numbers instead of two. Godot's 3D axes are:

| axis | positive direction | Godot name |
| --- | --- | --- |
| x | right | `Vector3.RIGHT` = (1, 0, 0) |
| y | **up** | `Vector3.UP` = (0, 1, 0) |
| z | towards you (out of the screen) | `Vector3.BACK` = (0, 0, 1) |

Two things trip up everyone coming from 2D:

- **y points up** in 3D (in 2D it pointed down). So gravity *lowers* `velocity.y` in 3D.
- **forward is negative z**: `Vector3.FORWARD` is `(0, 0, -1)`. Cameras and characters look down the -z axis.

The floor is the **x–z plane**: walking around means changing x and z, and y is height.

## The same math, one more number

Everything from the 2D vector lesson still works. Subtracting gives the arrow from A to B, `normalized()` makes it length 1, and the length uses Pythagoras with three parts:

```
length = √(x² + y² + z²)
(2, 3, 6): 4 + 9 + 36 = 49, √49 = 7
```

## Distance on the ground

Often you want to ignore height: "how far away is the enemy, if I don't care that it's standing on a hill?" Just set y to 0 before measuring:

```gdscript
var flat := b - a
flat.y = 0
flat.length()
```

Example: a = (0, 0, 0), b = (3, 10, 4). The straight distance is √(9 + 100 + 16) ≈ 11.2, but on the ground it's √(9 + 16) = 5.

## Your quest

1. `ground_distance(a: Vector3, b: Vector3) -> float`: the distance from a to b, ignoring height.
2. `ground_direction(a: Vector3, b: Vector3) -> Vector3`: the length-1 direction from a to b along the ground (y = 0).
