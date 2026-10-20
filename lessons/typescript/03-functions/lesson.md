---
title: Typed functions
xp: 15
---
# Functions with types

Give each **parameter** a type, and put the **return type** after the brackets:

```ts
function heal(hp: number, amount: number): number {
  return hp + amount;
}

heal(10, 5);      // 15
heal(10, "five"); // error: "five" isn't a number
```

You can also write a function as an **arrow function**:

```ts
const double = (n: number): number => n * 2;
```

`Math.max(a, b)` gives back the bigger of two numbers.

## Your quest

Write `damage(attack: number, defense: number): number`. It returns `attack - defense`, but never less than `0`.

- `damage(10, 3)` returns `7`
- `damage(2, 8)` returns `0`
