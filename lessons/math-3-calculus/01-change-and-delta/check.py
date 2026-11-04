d, ar, ds = ns.get("delta"), ns.get("avg_rate"), ns.get("deltas")
assert d and ar and ds, "Keep delta, avg_rate and deltas."
assert abs(d(2.5, 1.9) + 0.6) < 1e-12, f"delta(2.5, 1.9) should be -0.6 (after minus before), got {d(2.5, 1.9)!r}."
assert d(3, 10) == 7, "delta(3, 10) = 7."
assert ar(lambda s: 3 * s, 1, 4) == 3, "A straight line 3x changes by 3 per 1."
assert abs(ar(lambda x: x * x, 1, 3) - 4) < 1e-12, "x² from 1 to 3: (9 − 1) / (3 − 1) = 4."
assert abs(ar(lambda s: 2.5 - 0.002 * (s - 100), 100, 400) + 0.002) < 1e-12, "Falling loss must give a negative rate."
assert ds([2, 5, 4]) == [3, -1], f"deltas([2, 5, 4]) should be [3, -1], got {ds([2, 5, 4])!r}."
assert ds([7]) == [], "One value has no changes."
