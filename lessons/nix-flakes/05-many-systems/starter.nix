{
  description = "Works on Intel and ARM";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      forAllSystems = nixpkgs.lib.genAttrs [ "x86_64-linux" ];
    in {
      packages.x86_64-linux.default = nixpkgs.legacyPackages.x86_64-linux.hello;
    };
}
