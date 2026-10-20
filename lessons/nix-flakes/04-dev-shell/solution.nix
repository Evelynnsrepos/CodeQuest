{
  description = "A project with a dev shell";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }:
    let
      pkgs = nixpkgs.legacyPackages.x86_64-linux;
    in {
      devShells.x86_64-linux.default = pkgs.mkShell {
        packages = [ pkgs.git pkgs.python3 pkgs.ripgrep ];
        shellHook = ''
          echo "Welcome to the dev shell"
        '';
      };
    };
}
