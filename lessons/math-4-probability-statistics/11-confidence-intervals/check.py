import statistics
pc, ss, mc = ns.get("proportion_ci"), ns.get("sample_std"), ns.get("mean_ci")
assert pc and ss and mc, "Keep proportion_ci, sample_std and mean_ci."
lo, hi = pc(60, 100)
assert abs(lo - 0.50398) < 1e-4 and abs(hi - 0.69602) < 1e-4, f"proportion_ci(60, 100) ≈ (0.504, 0.696), got {(lo, hi)!r}."
lo, hi = pc(6, 10)
assert abs(lo - 0.2964) < 1e-3 and abs(hi - 0.9036) < 1e-3, "6 of 10: much wider."
xs = [70, 72, 68, 75, 65]
assert abs(ss(xs) - statistics.stdev(xs)) < 1e-12, f"sample_std divides by n − 1: ≈ 3.808, got {ss(xs)!r}."
lo, hi = mc(xs)
assert abs(lo - 66.662) < 1e-2 and abs(hi - 73.338) < 1e-2, f"mean_ci ≈ (66.66, 73.34), got {(lo, hi)!r}."
