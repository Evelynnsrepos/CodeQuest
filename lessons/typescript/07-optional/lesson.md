---
title: Optional values
xp: 20
---
# Maybe there, maybe not

Put `?` after a parameter name to make it **optional**. If it's left out, it's `undefined`:

```ts
function title(name: string, rank?: string): string {
  if (rank === undefined) {
    return name;
  }
  return `${rank} ${name}`;
}
```

Because of `strict` mode, TypeScript won't let you use `rank` as a string until you've checked it isn't `undefined`.

Two handy shortcuts:

- `a ?? b` gives `b` when `a` is `undefined` or `null`.
- `obj?.prop` reads `prop` only if `obj` exists, otherwise gives `undefined`.

Array `find` returns the first match, or `undefined` if there isn't one. So its type is `Hero | undefined`.

## Your quest

Write `hpOf(party: Hero[], name: string): number`. It finds the hero with that name and returns their `hp`, or `0` if nobody in the party has that name.

The starter doesn't compile yet: read the error, then handle the `undefined` case.
