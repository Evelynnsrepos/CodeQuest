assert "xp_needed" in ns, "Define a function called xp_needed."
f = ns["xp_needed"]
for level, want in [(1, 100), (5, 500), (12, 1200), (0, 0)]:
    got = f(level)
    assert got == want, f"xp_needed({level}) returned {got!r}, expected {want}."
