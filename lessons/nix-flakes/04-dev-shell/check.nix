{ result, prelude, expect }:
let
  out = prelude.outputsOf result;
  shell = out.devShells.x86_64-linux.default or null;
  names = map (p: p.pname or "?") (shell.packages or [ ]);
in [
  (expect (shell != null) "Add devShells.x86_64-linux.default.")
  (expect ((shell.madeWith or null) == "mkShell") "Make the shell with pkgs.mkShell { ... }.")
  (expect (builtins.all (n: builtins.elem n names) [ "git" "python3" "ripgrep" ])
    "packages should be [ pkgs.git pkgs.python3 pkgs.ripgrep ].")
  (expect (builtins.match ".*echo \"Welcome to the dev shell\".*" (builtins.replaceStrings [ "\n" ] [ " " ] (shell.shellHook or "")) != null)
    "shellHook should contain: echo \"Welcome to the dev shell\"")
]
