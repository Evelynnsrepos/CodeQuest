---
title: Attribute sets
xp: 15
---
# Attribute sets

Most Nix code is made of **attribute sets**: names with values, inside `{ }`. Every entry ends with a semicolon.

```nix
{
  name = "firefox";
  version = 140;
  unfree = false;
}
```

Sets can hold other sets. Writing a dotted name is a shortcut for that, so these two mean the same:

```nix
{ meta = { license = "MIT"; }; }
{ meta.license = "MIT"; }
```

That dotted style is what your NixOS config is full of, like `services.openssh.enable = true;`.

## Your quest

Make the file a set with:

- `name` set to `"codequest"`
- `version` set to `"1.0"`
- `meta.description` set to `"Learn Nix"`
- `meta.license` set to `"MIT"`
