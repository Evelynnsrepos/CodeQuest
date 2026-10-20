{
  description = "My own little tools";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in {
      packages.x86_64-linux = {
        default = pkgs.cowsay;
        greet = pkgs.writeShellScriptBin "greet" "echo Hello from my flake";
      };
    };
}
