import math
fd, cd, tg = ns.get("forward_diff"), ns.get("central_diff"), ns.get("tangent")
assert fd and cd and tg, "Keep forward_diff, central_diff and tangent."
sq = lambda x: x * x
assert abs(fd(sq, 3, 1) - 7) < 1e-9 and abs(fd(sq, 3, 0.01) - 6.01) < 1e-9, f"forward_diff(x², 3, 0.01) should be 6.01, got {fd(sq, 3, 0.01)!r}."
assert abs(cd(sq, 3) - 6) < 1e-6, f"central_diff(x², 3) should be about 6, got {cd(sq, 3)!r}."
assert abs(cd(math.sin, 0) - 1) < 1e-6, "Slope of sin at 0 is 1."
assert abs(cd(lambda x: 5 * x + 2, 10) - 5) < 1e-6, "A straight line's slope is the same everywhere."
m, b = tg(sq, 3)
assert abs(m - 6) < 1e-5 and abs(b + 9) < 1e-4, f"Tangent to x² at 3 is y = 6x − 9, got {(m, b)!r}."
