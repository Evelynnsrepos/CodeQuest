---
title: Merging sets and rec
xp: 20
---
# Updating and self-referencing sets

`//` merges two sets. Where both have a name, the right side wins:

```nix
{ editor = "nano"; shell = "bash"; } // { editor = "helix"; }
# { editor = "helix"; shell = "bash"; }
```

This is how you override defaults without rewriting them. (It's shallow: nested sets are replaced, not merged.)

A `rec` set can refer to its own attributes:

```nix
rec {
  pname = "hello";
  version = "2.12";
  name = "${pname}-${version}";
}
```

You'll see `rec` in older package definitions in nixpkgs.

## Your quest

- `settings`: `defaults` merged with a set that changes `editor` to `"helix"`, using `//`
- `package`: a `rec` set with `pname = "hello"`, `version = "2.12"` and `name` built from those two, giving `"hello-2.12"`
