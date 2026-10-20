---
title: Functions
xp: 20
---
# Functions

A Nix function has one argument, a colon, and a body:

```nix
x: x + 1
```

You call it by writing the argument after it, with a space: `(x: x + 1) 41` is `42`.

Most functions in nixpkgs take a **set** and pick names out of it. A `?` gives a default value:

```nix
{ name, greeting ? "Hello" }: "${greeting}, ${name}!"
```

Call it with a set: `f { name = "Nix"; }` gives `"Hello, Nix!"`.

Your `configuration.nix` is one of these: `{ config, pkgs, ... }: { ... }`. The `...` means "ignore any other names".

## Your quest

Make the file a set of two functions:

- `double`: takes a number and returns it times 2
- `greet`: takes a set with `name` and an optional `greeting` (default `"Hello"`) and returns `"<greeting>, <name>!"`
