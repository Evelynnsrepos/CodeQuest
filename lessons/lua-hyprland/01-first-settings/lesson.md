---
title: Your first settings
xp: 15
---
# Hello, hyprland.lua

Since **Hyprland 0.55** (May 2026), Hyprland is configured in Lua. Your config lives in `~/.config/hypr/hyprland.lua`. Older versions use `hyprland.conf`, which has a different syntax, so check yours with `hyprctl version`.

Hyprland gives your config a table called `hl` full of functions. In these lessons you use a **practice copy** of it: it records what you set and shows what Hyprland would apply, without touching your real desktop.

Most settings go through `hl.config()`, which takes a **table**. Tables can hold other tables, which is how settings are grouped:

```lua
hl.config({
    general = {
        gaps_in  = 5,     -- gap between windows
        gaps_out = 20,    -- gap around the screen edge
    },
})
```

## Your quest

Set these with `hl.config`:

- `general.gaps_in` to `4`
- `general.gaps_out` to `12`
- `general.border_size` to `2`
- `decoration.rounding` to `8`

Press **Run** to see what Hyprland would apply.
