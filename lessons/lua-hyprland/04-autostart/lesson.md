---
title: Autostart
xp: 20
---
# Start my bar when I log in

Some programs should start with Hyprland: a status bar, a wallpaper tool, the network icon. You don't want them to start every time the config reloads, only once at startup.

That's what **events** are for. `hl.on(event, fn)` stores a function and Hyprland calls it when the event happens:

```lua
hl.on("hyprland.start", function()
    hl.exec_cmd("waybar")
end)
```

The `function() ... end` is a function without a name, passed as a value. Its body doesn't run now; it runs later, when Hyprland starts. (`hl.exec_cmd` runs a command right away, while `hl.dsp.exec_cmd` is an action for a keybind.)

## Your quest

When Hyprland starts, run `waybar`, `hyprpaper` and `nm-applet`. Don't run anything outside the function.
