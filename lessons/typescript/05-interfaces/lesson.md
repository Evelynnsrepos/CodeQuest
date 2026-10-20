---
title: Objects and interfaces
xp: 20
---
# Describing the shape of an object

An **interface** names the shape of an object: which properties it has and their types.

```ts
interface Enemy {
  name: string;
  hp: number;
}

const slime: Enemy = { name: "Slime", hp: 8 };
slime.hp -= 3;      // fine
slime.mana = 10;    // error: Enemy has no 'mana'
```

To make a changed copy of an object, use the **spread** `...`:

```ts
const hurt: Enemy = { ...slime, hp: slime.hp - 1 };
```

## Your quest

1. Write an `interface Hero` with `name: string`, `hp: number` and `level: number`.
2. Write `levelUp(hero: Hero): Hero` that returns a **new** hero with `level` one higher and `hp` 10 higher. Don't change the hero that was passed in.
