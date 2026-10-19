local wanted = {
  { "XF86AudioRaiseVolume", "wpctl set-volume -l 1 @DEFAULT_AUDIO_SINK@ 5%+" },
  { "XF86AudioLowerVolume", "wpctl set-volume @DEFAULT_AUDIO_SINK@ 5%-" },
  { "XF86AudioMute", "wpctl set-mute @DEFAULT_AUDIO_SINK@ toggle" },
}
for _, w in ipairs(wanted) do
  local b = _hypr.find_bind(w[1])
  assert(b, ("There's no bind for %s."):format(w[1]))
  assert(b.action.dispatcher == "exec_cmd" and b.action.args == w[2], ("%s should run: %s"):format(w[1], w[2]))
  assert(b.opts.locked == true and b.opts.repeating == true, ("%s should have { locked = true, repeating = true }."):format(w[1]))
end
