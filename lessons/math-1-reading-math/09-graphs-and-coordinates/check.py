pt, og, fa = ns.get("points"), ns.get("on_graph"), ns.get("is_falling")
assert pt and og and fa, "Keep points, on_graph and is_falling."
assert pt(lambda x: x * x, [-1, 0, 2]) == [(-1, 1), (0, 0), (2, 4)], f"points(square, [-1, 0, 2]) should be [(-1, 1), (0, 0), (2, 4)], got {pt(lambda x: x * x, [-1, 0, 2])!r}."
d = lambda x: 2 * x
assert og(d, (3, 6)) is True and og(d, (6, 3)) is False, "(3, 6) is on y = 2x; (6, 3) is not. Across first!"
assert fa([(0, 2.5), (100, 1.8), (200, 1.4)]) is True, "2.5 → 1.8 → 1.4 is falling."
assert fa([(0, 2.5), (1, 2.6), (2, 1.0)]) is False, "It went up once, so not falling everywhere."
