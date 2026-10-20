{ result, expect, ... }: [
  (expect (builtins.isAttrs result) "Your file should be an attribute set, written with { }.")
  (expect ((result.name or null) == "codequest") "name should be \"codequest\".")
  (expect ((result.version or null) == "1.0") "version should be the string \"1.0\" (with quotes).")
  (expect (builtins.isAttrs (result.meta or null)) "Add a meta set, for example meta.description = ...;")
  (expect ((result.meta.description or null) == "Learn Nix") "meta.description should be \"Learn Nix\".")
  (expect ((result.meta.license or null) == "MIT") "meta.license should be \"MIT\".")
]
