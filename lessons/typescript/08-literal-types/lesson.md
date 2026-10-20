---
title: Type aliases and literal types
xp: 20
---
# Only these exact values

A **type alias** gives a type a name with `type`. A **literal type** allows only one exact value, and a union of them makes a short list of allowed values:

```ts
type Element = "fire" | "ice" | "storm";

let spell: Element = "fire";  // fine
spell = "water";              // error: not one of the three
```

This catches typos that plain `string` would let through. A `switch` works well with them:

```ts
switch (spell) {
  case "fire": return 3;
  case "ice": return 2;
  case "storm": return 4;
}
```

## Your quest

1. Write `type Direction = "up" | "down" | "left" | "right";`
2. Write `move(pos: Point, dir: Direction): Point` that returns a new point one step in that direction. `up` lowers `y` by 1, `down` raises `y` by 1, `left` lowers `x`, `right` raises `x`.

`Point` is already written for you.
