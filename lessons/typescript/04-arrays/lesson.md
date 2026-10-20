---
title: Arrays
xp: 15
---
# Lists of things

An array type is the element type followed by `[]`:

```ts
const loot: string[] = ["sword", "potion"];
const scores: number[] = [12, 40, 7];

loot.push("shield");    // fine
loot.push(42);          // error: 42 isn't a string
```

Loop over an array with `for...of`:

```ts
let total = 0;
for (const score of scores) {
  total += score;
}
```

## Your quest

Write `totalGold(bags: number[]): number` that adds up every bag of gold.

- `totalGold([5, 10, 20])` returns `35`
- `totalGold([])` returns `0`
