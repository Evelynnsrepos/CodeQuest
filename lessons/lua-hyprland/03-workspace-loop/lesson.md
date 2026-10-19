---
title: Workspaces with a loop
xp: 20
---
# Ten workspaces, four lines

Writing 20 almost identical binds by hand is boring and easy to get wrong. A `for` loop does it for you:

```lua
for i = 1, 3 do
    print("workspace " .. i)
end
```

Two actions you need:

- `hl.dsp.focus({ workspace = i })` switches to workspace `i`
- `hl.dsp.window.move({ workspace = i })` moves the focused window there

Keyboards have no "10" key, so workspace 10 goes on `0`. The `%` operator gives the remainder after dividing: `10 % 10` is `0`, and `3 % 10` is `3`.

## Your quest

For workspaces `1` to `10`, where `key = i % 10`:

- `mainMod + key` focuses workspace `i`
- `mainMod + SHIFT + key` moves the window to workspace `i`
