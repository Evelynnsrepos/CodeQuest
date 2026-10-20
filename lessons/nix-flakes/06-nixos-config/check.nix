{ result, prelude, expect }:
let
  out = prelude.outputsOf result;
  sys = out.nixosConfigurations.codequest or null;
  cfg = sys.config or { };
  installed = map (p: p.pname or "?") (cfg.environment.systemPackages or [ ]);
in [
  (expect (sys != null) "Add nixosConfigurations.codequest.")
  (expect ((sys._type or null) == "practice-nixos") "Make it with nixpkgs.lib.nixosSystem { ... }.")
  (expect (sys.system == "x86_64-linux") "Set system = \"x86_64-linux\";")
  (expect ((cfg.networking.hostName or null) == "codequest") "networking.hostName should be \"codequest\".")
  (expect (builtins.elem "git" installed && builtins.elem "helix" installed)
    "environment.systemPackages should contain git and helix.")
  (expect (builtins.all (f: builtins.elem f (cfg.nix.settings.experimental-features or [ ])) [ "nix-command" "flakes" ])
    "nix.settings.experimental-features should be [ \"nix-command\" \"flakes\" ].")
]
