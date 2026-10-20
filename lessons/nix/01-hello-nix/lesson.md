---
title: Hello, Nix
xp: 10
---
# Everything is an expression

Nix is the language NixOS, nixpkgs and flakes are written in. It's a little different from Python or Lua: a Nix file doesn't *run steps*, it **is one value**. Nix reads the file and works out (evaluates) that value.

The simplest Nix file is just a string:

```nix
"I am a whole Nix file"
```

Numbers, `true`/`false`, `null`, lists and strings are all values. Comments start with `#`.

CodeQuest evaluates your file with `nix-instantiate --eval --strict`, the same tool you can use in a terminal, and shows the result.

## Your quest

Change the string so the file evaluates to `"Hello, Nix!"`.
