# A practice nixpkgs for the Nix flakes lessons. Packages are small stand-in sets, so nothing is
# downloaded or built. CodeQuest calls your flake's outputs with these inputs.
let
  systems = [ "x86_64-linux" "aarch64-linux" "x86_64-darwin" "aarch64-darwin" ];

  genAttrs = names: f: builtins.listToAttrs (map (name: { inherit name; value = f name; }) names);

  versions = {
    hello = "2.12.2"; cowsay = "3.8.4"; git = "2.51.0"; python3 = "3.13.7"; nodejs = "22.20.0";
    ripgrep = "14.1.1"; htop = "3.4.1"; neovim = "0.11.4"; helix = "25.07.1"; vim = "9.1.1765";
    firefox = "144.0"; godot = "4.5"; lua = "5.4.7"; rustc = "1.90.0"; cargo = "1.90.0";
    fastfetch = "2.53.0"; curl = "8.16.0"; wget = "1.25.0"; gcc = "14.3.0"; gnumake = "4.4.1";
    jq = "1.8.1"; fd = "10.3.0"; bat = "0.25.0"; kitty = "0.43.1"; waybar = "0.14.0";
  };

  package = system: pname: version: extra: {
    type = "derivation";
    name = "${pname}-${version}";
    inherit pname version system;
    outPath = "/nix/store/practice-${pname}-${version}";
  } // extra;

  pkgsFor = system:
    builtins.mapAttrs (pname: version: package system pname version { }) versions // {
      inherit system;
      writeShellScriptBin = name: script:
        package system name "script" { inherit script; madeWith = "writeShellScriptBin"; };
      mkShell = args: package system (args.name or "nix-shell") "shell" (args // {
        madeWith = "mkShell";
        packages = args.packages or [ ];
      });
    };

  # Merge NixOS modules roughly like NixOS does: sets merge, lists join, the last plain value wins.
  isPkg = v: builtins.isAttrs v && (v.type or null) == "derivation";
  merge = values:
    if builtins.all (v: builtins.isAttrs v && !isPkg v) values then builtins.zipAttrsWith (_: merge) values
    else if builtins.all builtins.isList values then builtins.concatLists values
    else builtins.elemAt values (builtins.length values - 1);

  lib = {
    inherit genAttrs;
    nixosSystem = { system ? "x86_64-linux", modules, specialArgs ? { } }:
      let
        pkgs = pkgsFor system;
        args = { inherit config pkgs lib; options = { }; modulesPath = "/nix/store/practice-nixpkgs/nixos/modules"; } // specialArgs;
        config = merge (map (m: if builtins.isFunction m then m args else m) modules);
      in { _type = "practice-nixos"; inherit system config; };
  };

  nixpkgs = {
    inherit lib;
    legacyPackages = genAttrs systems pkgsFor;
    outPath = "/nix/store/practice-nixpkgs";
  };

  outputsOf = flake:
    let self = flake.outputs { inherit self nixpkgs; };
    in self;

  # What Run prints: packages as «name», dev shells and systems summarised.
  simplify = v:
    if isPkg v then
      (if (v.madeWith or null) == "mkShell" then "«dev shell with ${toString (map (p: p.pname or "?") v.packages)}»"
       else if (v.madeWith or null) == "writeShellScriptBin" then "«script ${v.pname}: ${v.script}»"
       else "«package ${v.name} for ${v.system}»")
    else if builtins.isAttrs v && (v._type or null) == "practice-nixos" then
      { system = v.system; config = simplify v.config; }
    else if builtins.isAttrs v then builtins.mapAttrs (_: simplify) v
    else if builtins.isList v then map simplify v
    else v;
in
{
  inherit nixpkgs outputsOf;
  inputs = { inherit nixpkgs; };
  isPackage = p: pname: system: isPkg p && p.pname == pname && p.system == system;
  show = flake:
    if !(builtins.isAttrs flake) then flake
    else {
      description = flake.description or "(no description yet)";
      inputs = flake.inputs or { };
      outputs = if builtins.isFunction (flake.outputs or null) then simplify (outputsOf flake)
                else "(outputs isn't a function yet)";
    };
}
