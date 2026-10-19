---
title: Window rules
xp: 20
---
# Rules for specific apps

`hl.window_rule()` changes how matching windows behave. A rule has a `name`, a `match` table saying which windows it's for, and the effects you want:

```lua
hl.window_rule({
    name  = "float-calculator",
    match = { class = "^(org.gnome.Calculator)$" },
    float = true,
})
```

`class` is a **pattern**: `^` means "starts here", `$` means "ends here", and `.*` means "anything". Find an app's class with `hyprctl clients`.

## Your quest

Add two rules:

1. Named `float-pavucontrol`: windows with class `^(pavucontrol)$` should `float`.
2. Named `suppress-maximize-events`: for every window (class `.*`), set `suppress_event = "maximize"` so apps can't maximize themselves.
