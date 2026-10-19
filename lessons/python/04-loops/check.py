assert "total_loot" in ns, "Define a function called total_loot."
f = ns["total_loot"]
for chests, want in [([3, 7, 2], 12), ([], 0), ([100], 100), ([5, 5, 5, 5], 20)]:
    got = f(list(chests))
    assert got == want, f"total_loot({chests}) returned {got!r}, expected {want}."
