---
title: Loops and slices
xp: 20
---
# Counting the loot

A **slice** like `&[u32]` lets a function look at a list of numbers without taking ownership of it. A `for` loop visits each item.

```rust
fn print_all(coins: &[u32]) {
    for c in coins {
        println!("{}", c);
    }
}
```

Inside the loop, `c` is a reference (`&u32`). Write `*c` to get the number itself.

## Your quest

Write `fn total_loot(chests: &[u32]) -> u32` that adds up every chest using a `for` loop.

- `total_loot(&[3, 7, 2])` returns `12`
- `total_loot(&[])` returns `0`
