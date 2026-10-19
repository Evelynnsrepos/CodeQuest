---
title: Mutable variables
xp: 10
---
# Variables that change

Variables are created with `let`. In Rust they **can't change** unless you say so with `mut`.

```rust
let gold = 50;        // fixed
let mut arrows = 10;  // can change
arrows -= 1;
println!("{}", arrows); // {} is replaced by the value
```

## Your quest

The starter code doesn't compile yet. Press **Run** to see Rust's error message, then fix it so the program prints `75`.
