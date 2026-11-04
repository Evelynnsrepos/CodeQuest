import math
pi, ex, p1 = ns.get("power_iteration"), ns.get("explained"), ns.get("pca_1d")
assert pi and ex and p1, "Keep power_iteration, explained and pca_1d."
v, lam = pi([[2, 1], [1, 2]])
assert abs(lam - 3) < 1e-6 and all(abs(abs(x) - 1 / math.sqrt(2)) < 1e-6 for x in v), f"Top eigenvector (0.707, 0.707), λ = 3. Got {v!r}, {lam!r}."
v, lam = pi([[5, 0, 0], [0, 1, 0], [0, 0, 2]])
assert abs(lam - 5) < 1e-6 and abs(abs(v[0]) - 1) < 1e-6, "Diagonal matrix: the biggest diagonal entry wins."
assert abs(ex([[2, 1], [1, 2]]) - 0.75) < 1e-6, "explained: 3 / 4."
z = p1([[1, 1], [2, 2.1], [3, 2.9], [4, 4.2]])
assert len(z) == 4 and abs(sum(z)) < 1e-9, "pca_1d: one number per point, centered (they sum to 0)."
assert z[0] < z[1] < z[2] < z[3] and abs(z[3] - 2.2) < 0.1, f"Points along the diagonal, in order: about [-2.1, -0.7, 0.6, 2.2]; got {[round(x, 2) for x in z]}."
