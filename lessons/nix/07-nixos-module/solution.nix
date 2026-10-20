{ config, pkgs, ... }:
{
  networking.hostName = "codequest";
  environment.systemPackages = with pkgs; [ git helix htop ];
  services.openssh.enable = true;
  system.stateVersion = "25.11";
}
