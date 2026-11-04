d2, i2, s2 = ns.get("det2"), ns.get("inverse2"), ns.get("solve2")
assert d2 and i2 and s2, "Keep det2, inverse2 and solve2."
assert d2([[2, 1], [1, 3]]) == 5 and d2([[1, 2], [2, 4]]) == 0, f"det2([[2,1],[1,3]]) should be 5, got {d2([[2, 1], [1, 3]])!r}."
inv = i2([[2, 1], [1, 3]])
want = [[0.6, -0.2], [-0.2, 0.4]]
assert all(abs(inv[i][j] - want[i][j]) < 1e-12 for i in range(2) for j in range(2)), f"inverse2 should be {want!r}, got {inv!r}."
try:
    i2([[1, 2], [2, 4]])
except ValueError:
    pass
else:
    raise AssertionError("inverse2 of a singular matrix should raise ValueError.")
x = s2([[2, 1], [1, 3]], [5, 10])
assert abs(x[0] - 1) < 1e-12 and abs(x[1] - 3) < 1e-12, f"solve2 should give [1, 3], got {x!r}."
