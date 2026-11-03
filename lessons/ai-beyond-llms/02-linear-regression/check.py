fl, ms = ns.get("fit_line"), ns.get("mse")
assert fl and ms, "Keep fit_line and mse."
a, b = fl([0, 1, 2, 3], [1, 3, 5, 7])
assert abs(a - 2) < 1e-9 and abs(b - 1) < 1e-9, f"Points on y = 2x + 1 should give (2, 1), got {(a, b)!r}."
a, b = fl([1, 2, 3], [2, 2, 5])
assert abs(a - 1.5) < 1e-9 and abs(b - 0) < 1e-9, f"fit_line([1,2,3], [2,2,5]) should be (1.5, 0.0), got {(a, b)!r}."
assert abs(ms([1, 2, 3], [2, 2, 5], 1.5, 0.0) - 0.5) < 1e-9, f"MSE there should be (0.25 + 1 + 0.25) / 3 = 0.5, got {ms([1, 2, 3], [2, 2, 5], 1.5, 0.0)!r}."
