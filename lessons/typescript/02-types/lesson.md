---
title: Variables and types
xp: 10
---
# Every value has a type

Make a variable with `let` if it will change and `const` if it won't. After the name you can write its **type**:

```ts
const heroName: string = "Evy";
let gold: number = 50;
let hasKey: boolean = false;
```

The three basic types are `string` (text), `number` (any number, whole or not) and `boolean` (`true` or `false`).

If you put the wrong kind of value in, TypeScript stops before your code even runs:

```ts
let gold: number = "lots"; // Type 'string' is not assignable to type 'number'.
```

TypeScript can also work out the type itself: `let gold = 50` is a `number` too. That's called **type inference**.

## Your quest

The starter has a type error. Press Run to see it, then fix it:

1. `level` must be a `number` with the value `5`.
2. `heroName` is a `string`, `isAlive` is a `boolean` set to `true`.
3. Print `level`.
