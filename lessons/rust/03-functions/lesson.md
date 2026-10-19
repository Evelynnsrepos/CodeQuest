---
title: Functions
xp: 15
---
# Levelling up

Functions start with `fn`. Rust needs the type of every parameter, and the return type after `->`.

```rust
fn double(n: u32) -> u32 {
    n * 2
}
```

The last expression in a function, **without a semicolon**, is its return value. `u32` is a whole number that can't be negative.

## Your quest

Write `fn xp_needed(level: u32) -> u32` that returns the level times 100.

- `xp_needed(1)` returns `100`
- `xp_needed(5)` returns `500`
