local handlers = _hypr.handlers["hyprland.start"]
assert(handlers and #handlers > 0, "Use hl.on(\"hyprland.start\", function() ... end).")
_hypr.start()
assert((_hypr.execs_before_start or 0) == 0,
  "Something ran straight away. Put every hl.exec_cmd inside the function so it only runs at startup.")
local ran = {}
for _, cmd in ipairs(_hypr.execs) do ran[cmd] = true end
for _, want in ipairs({ "waybar", "hyprpaper", "nm-applet" }) do
  assert(ran[want], ("%s doesn't start when Hyprland starts."):format(want))
end
