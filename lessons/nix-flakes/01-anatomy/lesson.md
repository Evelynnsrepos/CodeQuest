---
title: Anatomy of a flake
xp: 15
---
# What's in a flake.nix

A flake is a folder with a `flake.nix` that says exactly **what it depends on** and **what it provides**. Nix records the exact version of every input in `flake.lock`, so the same flake builds the same thing on every computer.

`flake.nix` is a set with three parts:

```nix
{
  description = "A short sentence about this flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";
  };

  outputs = { self, nixpkgs }: {
    # what this flake provides goes here
  };
}
```

- `inputs` are other flakes, written as URLs. `github:NixOS/nixpkgs/nixos-unstable` is the nixos-unstable branch of nixpkgs. Inputs have to be written out literally; you can't compute them.
- `outputs` is a **function**. Nix fetches the inputs and passes them in by name.

In these lessons your code is a `flake.nix`. CodeQuest gives your `outputs` a **practice nixpkgs**: packages are small stand-ins, so nothing is downloaded or built, and **Run** shows the outputs your flake produces.

On your computer, flakes need `nix-command` and `flakes` turned on. On NixOS add this to your configuration: `nix.settings.experimental-features = [ "nix-command" "flakes" ];`

## Your quest

- Add a `description` (any text)
- Add the `nixpkgs` input pointing at `github:NixOS/nixpkgs/nixos-unstable`
