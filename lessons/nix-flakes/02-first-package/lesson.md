---
title: Your first package
xp: 20
---
# Providing a package

Outputs have standard names that the `nix` command knows. Packages go in `packages.<system>.<name>`, where the system is your kind of computer, like `x86_64-linux`.

nixpkgs keeps its packages in `legacyPackages.<system>`, so the hello package is:

```nix
nixpkgs.legacyPackages.x86_64-linux.hello
```

The package called `default` is the one `nix build` and `nix run` pick when you don't name one.

In these lessons your code is a `flake.nix`. CodeQuest gives your `outputs` a **practice nixpkgs**: packages are small stand-ins, so nothing is downloaded or built, and **Run** shows the outputs your flake produces.

On your computer you'd now run `nix run` in the flake's folder and see "Hello, world!".

## Your quest

Make `packages.x86_64-linux.default` the `hello` package from nixpkgs.
