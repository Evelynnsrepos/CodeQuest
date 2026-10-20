---
title: A dev shell
xp: 20
---
# nix develop

A dev shell gives you the tools for a project without installing them on your system. Run `nix develop` in the folder and you're in a shell where they're all available; leave it and they're gone.

Dev shells go in `devShells.<system>.<name>` and are made with `pkgs.mkShell`:

```nix
devShells.x86_64-linux.default = pkgs.mkShell {
  packages = [ pkgs.nodejs ];
  shellHook = ''
    echo "Ready to hack"
  '';
};
```

`shellHook` runs when the shell starts. The `'' ... ''` quotes make a multi-line string.

In these lessons your code is a `flake.nix`. CodeQuest gives your `outputs` a **practice nixpkgs**: packages are small stand-ins, so nothing is downloaded or built, and **Run** shows the outputs your flake produces.

## Your quest

Make `devShells.x86_64-linux.default` a `mkShell` with:

- `packages`: `git`, `python3` and `ripgrep`
- a `shellHook` that contains `echo "Welcome to the dev shell"`
