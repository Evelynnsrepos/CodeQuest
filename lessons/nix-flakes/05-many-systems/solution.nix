{
  description = "Works on Intel and ARM";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      forAllSystems = nixpkgs.lib.genAttrs [ "x86_64-linux" "aarch64-linux" ];
    in {
      packages = forAllSystems (system: {
        default = nixpkgs.legacyPackages.${system}.hello;
      });
      devShells = forAllSystems (system:
        let pkgs = nixpkgs.legacyPackages.${system};
        in { default = pkgs.mkShell { packages = [ pkgs.git ]; }; });
    };
}
