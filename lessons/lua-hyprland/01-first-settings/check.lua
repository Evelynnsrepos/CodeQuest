local c = _hypr.config
assert(type(c.general) == "table", "Put gaps_in, gaps_out and border_size inside a general = { ... } table.")
assert(c.general.gaps_in == 4, ("general.gaps_in should be 4, but it's %s."):format(tostring(c.general.gaps_in)))
assert(c.general.gaps_out == 12, ("general.gaps_out should be 12, but it's %s."):format(tostring(c.general.gaps_out)))
assert(c.general.border_size == 2, ("general.border_size should be 2, but it's %s."):format(tostring(c.general.border_size)))
assert(type(c.decoration) == "table", "rounding goes in its own decoration = { ... } table, next to general.")
assert(c.decoration.rounding == 8, ("decoration.rounding should be 8, but it's %s."):format(tostring(c.decoration.rounding)))
