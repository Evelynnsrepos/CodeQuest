a, t = ns.get("is_allowed"), ns.get("lethal_trifecta")
assert a and t, "Keep is_allowed and lethal_trifecta."
root = "/srv/data"
cases = [("a.txt", True), ("x/y/z.txt", True), (".", True), ("/srv/data/b.txt", True), ("../etc/shadow", False),
         ("x/../../data2/f", False), ("/srv/data-other/f", False), ("/etc/passwd", False), ("x/../y.txt", True)]
for path, want in cases:
    got = a(path, root)
    assert got is want, f"is_allowed({path!r}, {root!r}) returned {got!r}, expected {want}."
assert t([{"private_data"}, {"untrusted_input"}, {"sends_out"}]) is True, "Three tools, one leg each, together form the trifecta."
assert t([{"private_data", "untrusted_input", "sends_out"}]) is True, "One tool with all three legs is a trifecta too."
assert t([{"private_data"}, {"untrusted_input"}]) is False, "Without a way to send data out, it's not the trifecta."
assert t([]) is False, "No tools, no trifecta."
