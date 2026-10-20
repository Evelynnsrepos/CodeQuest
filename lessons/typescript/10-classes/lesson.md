---
title: Classes
xp: 25
---
# Bundling data and behaviour

A **class** is a blueprint for objects that have both data (properties) and functions (methods):

```ts
class Counter {
  private count = 0;

  add(n: number): void {
    this.count += n;
  }

  get total(): number {
    return this.count;
  }
}

const c = new Counter();
c.add(3);
c.count = 99;   // error: 'count' is private
```

`private` means only code inside the class can touch it. `void` means a method returns nothing. Inside a method, `this` is the object itself.

Useful array methods: `items.includes(x)` (is it there?), `items.indexOf(x)` (where, or `-1`), `items.splice(i, 1)` (remove one item at `i`).

## Your quest

Write a class `Inventory` with:

- a `private items: string[]` that starts empty
- `add(item: string): void`
- `has(item: string): boolean`
- `remove(item: string): boolean` that removes one copy and returns `true`, or returns `false` if the item wasn't there
- `count(): number`
