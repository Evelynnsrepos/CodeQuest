import math
t, el, hl = ns.get("table"), ns.get("estimate_limit"), ns.get("has_limit")
assert t and el and hl, "Keep table, estimate_limit and has_limit."
g = lambda x: (x * x - 1) / (x - 1)
r = t(g, 1, [0.1, 0.01, -0.01])
assert len(r) == 3 and abs(r[0] - 2.1) < 1e-9 and abs(r[2] - 1.99) < 1e-9, f"table(g, 1, [0.1, 0.01, -0.01]) should be about [2.1, 2.01, 1.99], got {r!r}."
assert abs(el(g, 1) - 2) < 1e-4, f"The limit of (x²−1)/(x−1) at 1 is 2, got {el(g, 1)!r}."
assert abs(el(lambda x: math.sin(x) / x, 0) - 1) < 1e-4, "sin(x)/x heads to 1 at 0."
assert hl(g, 1) is True, "(x²−1)/(x−1) has a limit at 1."
assert hl(lambda x: abs(x) / x, 0) is False, "|x|/x is −1 from the left and +1 from the right: no limit."
