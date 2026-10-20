{ result, expect, ... }: [
  (expect (builtins.isFunction (result.double or null)) "double should be a function, like x: ...")
  (expect (result.double 21 == 42) "double 21 should be 42.")
  (expect (result.double 0 == 0) "double 0 should be 0.")
  (expect (builtins.isFunction (result.greet or null)) "greet should be a function that takes a set.")
  (expect ((builtins.functionArgs result.greet) ? name) "greet should take { name, ... }.")
  (expect ((builtins.functionArgs result.greet).greeting or false) "greeting should have a default: greeting ? \"Hello\"")
  (expect (result.greet { name = "Nix"; } == "Hello, Nix!") "greet { name = \"Nix\"; } should be \"Hello, Nix!\".")
  (expect (result.greet { name = "Nix"; greeting = "Hi"; } == "Hi, Nix!") "greet { name = \"Nix\"; greeting = \"Hi\"; } should be \"Hi, Nix!\".")
]
