---
title: Keybinds
xp: 20
---
# Shortcuts

`hl.bind(keys, action)` connects a key combo to an **action** (Hyprland calls them dispatchers). Actions live in `hl.dsp`:

```lua
hl.bind("SUPER + Q", hl.dsp.exec_cmd("kitty"))   -- open a terminal
hl.bind("SUPER + C", hl.dsp.window.close())      -- close the focused window
```

Store things you reuse in `local` variables, and glue strings together with `..`:

```lua
local mainMod = "SUPER"
hl.bind(mainMod .. " + Q", hl.dsp.exec_cmd(terminal))   -- same as "SUPER + Q"
```

Then changing `mainMod` to `"ALT"` updates every bind at once.

## Your quest

Using the variables, add three binds:

- `mainMod + Q` runs the `terminal`
- `mainMod + E` runs the `fileManager`
- `mainMod + C` closes the window
