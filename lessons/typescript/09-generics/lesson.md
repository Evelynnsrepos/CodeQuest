---
title: Generics
xp: 25
---
# Functions that work for any type

Sometimes a function doesn't care what's inside an array, but you still want the types kept. A **generic** type parameter, written `<T>`, stands for "whatever type the caller uses":

```ts
function last<T>(items: T[]): T | undefined {
  return items[items.length - 1];
}

const word = last(["a", "b"]);  // word is string | undefined
const num = last([1, 2, 3]);    // num is number | undefined
```

TypeScript fills in `T` from the arguments, so you rarely write it yourself. You've already used generics: `Array<number>` is another way to write `number[]`.

## Your quest

Write `firstOr<T>(items: T[], fallback: T): T`. It returns the first item, or `fallback` if the array is empty.

- `firstOr([3, 9], 0)` returns `3`
- `firstOr([], "none")` returns `"none"`
