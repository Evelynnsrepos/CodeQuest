---
title: Lists and builtins
xp: 20
---
# Lists

Lists go in `[ ]`, separated by spaces, not commas:

```nix
[ 1 2 3 "four" ]
```

Nix has no loops. Instead you hand a function to a builtin:

- `map f list` calls `f` on every item: `map (x: x * 10) [ 1 2 ]` is `[ 10 20 ]`
- `builtins.filter f list` keeps the items where `f` is `true`
- `builtins.foldl' f start list` combines all items into one value, for example a sum: `builtins.foldl' (a: b: a + b) 0 [ 1 2 3 ]` is `6`
- `builtins.length list` counts the items

Watch out: `x/2` without spaces is a **path** in Nix. Write `x / 2`.

## Your quest

Using `nums` from the starter, make a set with:

- `doubled`: every number times 2
- `big`: only the numbers greater than 3
- `total`: the sum of all numbers
- `count`: how many numbers there are
