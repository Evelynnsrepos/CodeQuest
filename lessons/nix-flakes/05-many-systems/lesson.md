---
title: Every system at once
xp: 25
---
# More than one kind of computer

`packages.x86_64-linux` only works on Intel/AMD Linux. A Raspberry Pi or an ARM laptop is `aarch64-linux`. Instead of copying everything per system, flakes build the set with a function.

`nixpkgs.lib.genAttrs` takes a list of names and a function, and makes a set with one entry per name:

```nix
nixpkgs.lib.genAttrs [ "a" "b" ] (name: "hi ${name}")
# { a = "hi a"; b = "hi b"; }
```

So a common pattern is:

```nix
let
  forAllSystems = nixpkgs.lib.genAttrs [ "x86_64-linux" "aarch64-linux" ];
in {
  packages = forAllSystems (system: {
    default = nixpkgs.legacyPackages.${system}.hello;
  });
}
```

`legacyPackages.${system}` picks the right nixpkgs for each system.

In these lessons your code is a `flake.nix`. CodeQuest gives your `outputs` a **practice nixpkgs**: packages are small stand-ins, so nothing is downloaded or built, and **Run** shows the outputs your flake produces.

## Your quest

Using `forAllSystems` for `x86_64-linux` and `aarch64-linux`:

- `packages.<system>.default` is `hello` for that system
- `devShells.<system>.default` is a `mkShell` with `git` for that system
