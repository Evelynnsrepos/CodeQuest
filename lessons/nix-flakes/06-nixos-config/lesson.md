---
title: Your NixOS system as a flake
xp: 30
---
# nixosConfigurations

A flake can hold your whole NixOS system. It goes in `nixosConfigurations.<hostname>`, made with `nixpkgs.lib.nixosSystem`:

```nix
nixosConfigurations.mypc = nixpkgs.lib.nixosSystem {
  system = "x86_64-linux";
  modules = [ ./configuration.nix ];
};
```

`modules` is a list of NixOS modules, like the one you wrote in the Nix course. Usually it's `./configuration.nix`, but a module can also be written right there in the list.

Then `sudo nixos-rebuild switch --flake .#mypc` builds and switches to it, using the exact nixpkgs version in `flake.lock`. `nix flake update` moves the lock to newer versions.

To start on your own machine: `cd /etc/nixos`, run `nix flake init`, put this in the `flake.nix`, then rebuild with `--flake`.

In these lessons your code is a `flake.nix`. CodeQuest gives your `outputs` a **practice nixpkgs**: packages are small stand-ins, so nothing is downloaded or built, and **Run** shows the outputs your flake produces.

## Your quest

Make `nixosConfigurations.codequest` for `x86_64-linux` with one inline module that:

- sets `networking.hostName` to `"codequest"`
- installs `git` and `helix`
- turns on flakes: `nix.settings.experimental-features = [ "nix-command" "flakes" ];`
