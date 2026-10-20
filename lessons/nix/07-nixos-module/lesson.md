---
title: A NixOS module
xp: 25
---
# What configuration.nix really is

Now you can read your own `/etc/nixos/configuration.nix`. It's a **function** that takes a set (with `config`, `pkgs` and more) and returns a set of options:

```nix
{ config, pkgs, ... }:
{
  networking.hostName = "nixos";
  environment.systemPackages = [ pkgs.git pkgs.htop ];
}
```

`pkgs` is nixpkgs, so `pkgs.git` is the git package. `with pkgs;` puts everything in `pkgs` in scope, so `with pkgs; [ git htop ]` is the same list. NixOS calls your function, merges the result with every other module, and builds the system from it.

Here the check calls your module with a practice `pkgs` instead of building anything.

## Your quest

Write a module that:

- sets `networking.hostName` to `"codequest"`
- installs `git`, `helix` and `htop` with `environment.systemPackages`
- turns on `services.openssh.enable`
- sets `system.stateVersion` to `"25.11"`
