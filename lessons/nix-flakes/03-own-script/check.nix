{ result, prelude, expect }:
let
  out = prelude.outputsOf result;
  ps = out.packages.x86_64-linux or { };
in [
  (expect (prelude.isPackage (ps.default or null) "cowsay" "x86_64-linux") "packages.x86_64-linux.default should be pkgs.cowsay.")
  (expect (ps ? greet) "Add a package called greet.")
  (expect ((ps.greet.madeWith or null) == "writeShellScriptBin") "Make greet with pkgs.writeShellScriptBin.")
  (expect (ps.greet.pname == "greet") "The script's command should be called \"greet\" (the first argument).")
  (expect (ps.greet.script == "echo Hello from my flake") "The script should be: echo Hello from my flake")
]
