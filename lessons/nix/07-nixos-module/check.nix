{ result, expect, ... }:
let
  pkgs = builtins.listToAttrs (map (n: { name = n; value = "pkgs.${n}"; })
    [ "git" "helix" "htop" "vim" "neovim" "firefox" "curl" "wget" "python3" "fastfetch" "ripgrep" "godot" ]);
  isModule = builtins.isFunction result;
  cfg = result { config = { }; inherit pkgs; lib = { }; options = { }; modulesPath = ""; };
  installed = cfg.environment.systemPackages or [ ];
in [
  (expect isModule "A module is a function: start the file with { config, pkgs, ... }:")
  (expect ((cfg.networking.hostName or null) == "codequest") "networking.hostName should be \"codequest\".")
  (expect (builtins.isList installed && builtins.all (p: builtins.elem p installed) [ "pkgs.git" "pkgs.helix" "pkgs.htop" ])
    "environment.systemPackages should contain pkgs.git, pkgs.helix and pkgs.htop.")
  (expect ((cfg.services.openssh.enable or false) == true) "Set services.openssh.enable = true;")
  (expect ((cfg.system.stateVersion or null) == "25.11") "system.stateVersion should be \"25.11\".")
]
