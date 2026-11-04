---
title: Ammo and reloading
xp: 20
---
# Click. Empty.

Most shooters have two ammo counts:

- `magazine`: bullets in the gun right now (at most `magazine_size`)
- `reserve`: spare bullets you carry

Reloading moves bullets from the reserve into the magazine, but only as many as **fit**, and only as many as you **have**. The amount to move is the smaller of two numbers:

```
needed = magazine_size - magazine     (empty space in the magazine)
moved  = min(needed, reserve)
```

Two examples with `magazine_size = 12`:

- magazine 4, reserve 50: needed = 8, moved = min(8, 50) = **8**. Magazine 12, reserve 42.
- magazine 0, reserve 5: needed = 12, moved = min(12, 5) = **5**. Magazine 5, reserve 0.

## Your quest

1. `fire() -> bool`: if `magazine` is `0`, return `false`. Otherwise use up one bullet and return `true`.
2. `reload()`: move bullets from `reserve` into `magazine` with the formula above.
