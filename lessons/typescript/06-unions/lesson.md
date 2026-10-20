---
title: Union types and narrowing
xp: 20
---
# One thing or another

A **union type** says a value can be one of several types. Write them with `|`:

```ts
let id: number | string;
id = 7;       // fine
id = "seven"; // also fine
```

Before you use it, check which one you have with `typeof`. Inside the `if`, TypeScript knows the exact type. That's called **narrowing**:

```ts
function show(id: number | string): string {
  if (typeof id === "number") {
    return "#" + id.toFixed(0);   // id is a number here
  }
  return id.toUpperCase();        // and a string here
}
```

A **template string** uses backticks and `${...}` to put values into text: `` `${count} coins` ``.

## Your quest

A chest holds either gold (a `number`) or an item name (a `string`). Write `describeReward(reward: number | string): string`:

- `describeReward(50)` returns `"50 gold"`
- `describeReward("Fire Sword")` returns `"Item: Fire Sword"`
