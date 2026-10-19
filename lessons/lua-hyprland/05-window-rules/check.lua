local function rule(name)
  for _, r in ipairs(_hypr.window_rules) do if r.name == name then return r end end
end
local p = rule("float-pavucontrol")
assert(p, "There's no window rule named float-pavucontrol.")
assert(type(p.match) == "table" and p.match.class == "^(pavucontrol)$", "float-pavucontrol should match class \"^(pavucontrol)$\".")
assert(p.float == true, "float-pavucontrol should set float = true.")
local s = rule("suppress-maximize-events")
assert(s, "There's no window rule named suppress-maximize-events.")
assert(type(s.match) == "table" and s.match.class == ".*", "suppress-maximize-events should match every window with class \".*\".")
assert(s.suppress_event == "maximize", "suppress-maximize-events should set suppress_event = \"maximize\".")
