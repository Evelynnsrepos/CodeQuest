ii, idist = ns.get("in_interval"), ns.get("is_distribution")
assert ii and idist, "Keep in_interval and is_distribution."
cases = [(1, "[0, 1)", False), (1, "[0, 1]", True), (0, "(0, 1]", False), (0.5, "(0, 1)", True), (-0.5, "(-1, 0]", True),
         (2, "[0, 1]", False), (0, "[0, 1)", True)]
for x, t, want in cases:
    got = ii(x, t)
    assert got is want, f"in_interval({x}, {t!r}) should be {want}, got {got!r}."
assert idist([0.2, 0.3, 0.5]) is True, "[0.2, 0.3, 0.5] is a valid distribution."
assert idist([0.7, 0.7, -0.4]) is False, "It sums to 1 but has a negative entry: not a distribution."
assert idist([0.5, 0.4]) is False, "It doesn't sum to 1."
