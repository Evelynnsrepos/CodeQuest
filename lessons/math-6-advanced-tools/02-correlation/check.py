co, r2, mc = ns.get("correlation"), ns.get("r_squared"), ns.get("most_correlated")
assert co and r2 and mc, "Keep correlation, r_squared and most_correlated."
h, s = [1, 2, 3, 4, 5], [50, 55, 65, 70, 80]
assert abs(co(h, s) - 0.99340) < 1e-4, f"r ≈ 0.993, got {co(h, s)!r}."
assert abs(co([x * 60 for x in h], s) - co(h, s)) < 1e-12, "Changing units must not change r."
assert abs(co([1, 2, 3], [6, 4, 2]) + 1) < 1e-12, "A perfect falling line → −1."
assert abs(co([-2, -1, 0, 1, 2], [4, 1, 0, 1, 4])) < 1e-12, "y = x² here gives r = 0: r only sees straight lines."
assert abs(r2(h, s) - 0.99340 ** 2) < 1e-3, "r_squared = r²."
cols = {"rain": [5, 4, 3, 2, 1], "noise": [3, 1, 4, 1, 5], "sun": [1, 2, 3, 4, 6]}
assert mc(cols, s) == "rain", "Use the absolute value: a strong negative correlation counts."
