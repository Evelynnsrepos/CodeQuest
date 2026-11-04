import math
nd, d = ns.get("numeric_derivative"), ns.get("df")
assert nd and d, "Keep numeric_derivative and df."
got = nd(math.sin, 0.0)
assert abs(got - 1) < 1e-6, f"numeric_derivative(math.sin, 0) returned {got!r}, expected about 1 (the slope of sin at 0)."
got = nd(lambda x: x ** 3, 2.0)
assert abs(got - 12) < 1e-4, f"numeric_derivative(x³, 2) returned {got!r}, expected about 12."
for x in [-3, 0, 1.5, 10]:
    assert abs(d(x) - (6 * x - 4)) < 1e-9, f"df({x}) returned {d(x)!r}. Differentiate 3x² − 4x + 7 term by term."
m = ns.get("minimum_x")
assert isinstance(m, (int, float)) and abs(m - 2 / 3) < 1e-6, f"minimum_x is {m!r}. Solve df(x) = 0 for x (a fraction is fine, e.g. 2 / 3)."
