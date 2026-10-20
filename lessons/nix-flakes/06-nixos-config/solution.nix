{
  description = "My NixOS machine";

  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixos-unstable";

  outputs = { self, nixpkgs }: {
    nixosConfigurations.codequest = nixpkgs.lib.nixosSystem {
      system = "x86_64-linux";
      modules = [
        ({ config, pkgs, ... }: {
          networking.hostName = "codequest";
          environment.systemPackages = with pkgs; [ git helix ];
          nix.settings.experimental-features = [ "nix-command" "flakes" ];
        })
      ];
    };
  };
}
