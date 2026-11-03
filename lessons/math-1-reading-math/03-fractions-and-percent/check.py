ap, pc, po = ns.get("as_percent"), ns.get("percent_change"), ns.get("percent_of")
assert ap and pc and po, "Keep as_percent, percent_change and percent_of."
assert abs(ap(3, 4) - 75) < 1e-9, f"as_percent(3, 4) should be 75, got {ap(3, 4)!r}."
assert abs(pc(2.5, 1.5) - (-40)) < 1e-9, f"percent_change(2.5, 1.5) should be -40, got {pc(2.5, 1.5)!r}."
assert abs(pc(50, 75) - 50) < 1e-9, "From 50 to 75 is +50%."
assert abs(po(20, 50) - 10) < 1e-9, f"20% of 50 is 10, got {po(20, 50)!r}."
