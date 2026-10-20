{ result, prelude, expect }: [
  (expect (builtins.isAttrs result) "A flake.nix is one set: { description = ...; inputs = ...; outputs = ...; }")
  (expect (builtins.isString (result.description or null) && result.description != "") "Add a description string.")
  (expect ((result.inputs.nixpkgs.url or null) == "github:NixOS/nixpkgs/nixos-unstable")
    "inputs.nixpkgs.url should be \"github:NixOS/nixpkgs/nixos-unstable\".")
  (expect (builtins.isFunction (result.outputs or null)) "outputs should be a function: { self, nixpkgs }: { ... }")
  (expect (builtins.isAttrs (prelude.outputsOf result)) "outputs should return a set.")
]
