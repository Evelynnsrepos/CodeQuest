---
title: let, in and strings
xp: 15
---
# Naming things with let

`let ... in` gives names to values, then uses them in the expression after `in`:

```nix
let
  user = "nixer";
in
  "/home/" + user
```

Strings can also pull values in with `${ }`, which is called interpolation. This is the same as above:

```nix
"/home/${user}"
```

When a set needs an attribute with the same name as a variable, `inherit` saves typing: `inherit user;` means `user = user;`.

## Your quest

Using the `let` block in the starter, make the file a set with:

- `user`: use `inherit` to copy it from the `let`
- `home`: `"/home/"` followed by the user, built with `${user}`
- `config`: the home folder followed by `/.config`, built from `home`

Pick any user name you like.
