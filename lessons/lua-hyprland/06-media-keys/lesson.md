---
title: Media keys and helpers
xp: 25
---
# Volume keys without repeating yourself

`hl.bind` takes an optional third argument with extra options:

```lua
hl.bind("XF86AudioMute", hl.dsp.exec_cmd("wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle"),
        { locked = true, repeating = true })
```

`locked` makes the key work on the lock screen, and `repeating` repeats while you hold it. Typing that options table on every line gets old, so write your own **function**:

```lua
local function say(word)
    print("Hyprland says " .. word)
end
```

## Your quest

1. Write `local function media(key, cmd)` that calls `hl.bind(key, hl.dsp.exec_cmd(cmd), { locked = true, repeating = true })`.
2. Use it for these three keys:

| Key | Command |
| --- | --- |
| `XF86AudioRaiseVolume` | `wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+` |
| `XF86AudioLowerVolume` | `wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-` |
| `XF86AudioMute` | `wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle` |

## Use it for real

You now know enough to write your own config. Copy your code into `~/.config/hypr/hyprland.lua` (Hyprland 0.55 or newer), save, and run `hyprctl reload` if it doesn't pick up the change. Big configs can be split into files and loaded with `require("keybinds")`. The [Hyprland wiki](https://wiki.hypr.land/configuring/) lists every setting, and Hyprland's [example config](https://github.com/hyprwm/Hyprland/blob/main/example/hyprland.lua) is a good starting point.
