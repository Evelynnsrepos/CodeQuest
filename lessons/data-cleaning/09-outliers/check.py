import statistics
f, o, z = ns.get("fences"), ns.get("outliers"), ns.get("z_outliers")
assert f and o and z, "Keep fences, outliers and z_outliers."
prices = [3.2, 2.9, 3.5, 3.1, 99999, 3.3]
q1, _, q3 = statistics.quantiles(prices, n=4)
lo, hi = f(prices)
assert abs(lo - (q1 - 1.5 * (q3 - q1))) < 1e-9 and abs(hi - (q3 + 1.5 * (q3 - q1))) < 1e-9, f"fences: Q1 − 1.5·IQR and Q3 + 1.5·IQR. Got {(lo, hi)!r}."
assert o(prices) == [4], f"outliers(prices) should be [4], got {o(prices)!r}."
assert o([10, 11, 12, 13, 14, 15, -50]) == [6], "Low outliers count too."
assert z(prices) == [], "With 6 values the huge one inflates the std so much it hides itself: z_outliers finds nothing."
xs = [10] * 30 + [11] * 30 + [100]
assert z(xs) == [60], "With more data, z-scores can work."
