---
title: A package of your own
xp: 20
---
# let pkgs = ...

Typing `nixpkgs.legacyPackages.x86_64-linux` every time gets old. Flakes usually start `outputs` with a `let`:

```nix
outputs = { self, nixpkgs }:
  let
    pkgs = nixpkgs.legacyPackages.x86_64-linux;
  in {
    packages.x86_64-linux.default = pkgs.hello;
  };
```

nixpkgs also has helpers that make packages for you. `pkgs.writeShellScriptBin name script` makes a package with one command called `name` that runs the shell script:

```nix
pkgs.writeShellScriptBin "hi" "echo hi there"
```

A flake can have many packages. You pick one with `#`: `nix run .#hi`.

In these lessons your code is a `flake.nix`. CodeQuest gives your `outputs` a **practice nixpkgs**: packages are small stand-ins, so nothing is downloaded or built, and **Run** shows the outputs your flake produces.

## Your quest

Add a `let` with `pkgs`, then provide two packages for `x86_64-linux`:

- `default`: `pkgs.cowsay`
- `greet`: a script made with `writeShellScriptBin` whose command is called `greet` and that runs `echo Hello from my flake`
