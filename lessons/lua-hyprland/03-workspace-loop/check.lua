for i = 1, 10 do
  local key = i % 10
  local f = _hypr.find_bind("SUPER + " .. key)
  assert(f, ("There's no bind for SUPER + %d."):format(key))
  assert(f.action.dispatcher == "focus" and type(f.action.args) == "table" and f.action.args.workspace == i,
    ("SUPER + %d should use hl.dsp.focus({ workspace = %d })."):format(key, i))
  local m = _hypr.find_bind("SUPER + SHIFT + " .. key)
  assert(m, ("There's no bind for SUPER + SHIFT + %d."):format(key))
  assert(m.action.dispatcher == "window.move" and type(m.action.args) == "table" and m.action.args.workspace == i,
    ("SUPER + SHIFT + %d should use hl.dsp.window.move({ workspace = %d })."):format(key, i))
end
