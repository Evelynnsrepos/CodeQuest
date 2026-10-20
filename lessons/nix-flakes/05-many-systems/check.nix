{ result, prelude, expect }:
let
  out = prelude.outputsOf result;
  systems = [ "x86_64-linux" "aarch64-linux" ];
  shellOk = s: let sh = out.devShells.${s}.default or { }; in
    (sh.madeWith or null) == "mkShell" && builtins.any (p: prelude.isPackage p "git" s) (sh.packages or [ ]);
in [
  (expect (builtins.all (s: out ? packages.${s}) systems) "packages should have both x86_64-linux and aarch64-linux. Use forAllSystems.")
  (expect (builtins.all (s: prelude.isPackage (out.packages.${s}.default or null) "hello" s) systems)
    "Each system's default package should be hello for that system: nixpkgs.legacyPackages.\${system}.hello")
  (expect (builtins.all (s: out ? devShells.${s}) systems) "devShells should have both systems too.")
  (expect (builtins.all shellOk systems) "Each system's dev shell should be a mkShell with that system's git.")
]
