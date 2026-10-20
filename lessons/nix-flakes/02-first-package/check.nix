{ result, prelude, expect }:
let out = prelude.outputsOf result;
in [
  (expect (out ? packages.x86_64-linux) "Add packages.x86_64-linux to your outputs.")
  (expect (out.packages.x86_64-linux ? default) "Add a package called default: packages.x86_64-linux.default = ...;")
  (expect (prelude.isPackage out.packages.x86_64-linux.default "hello" "x86_64-linux")
    "packages.x86_64-linux.default should be nixpkgs.legacyPackages.x86_64-linux.hello.")
]
