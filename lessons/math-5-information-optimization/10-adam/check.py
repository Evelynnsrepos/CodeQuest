ad = ns.get("adam_step")
assert ad, "Keep adam_step."
th, m, v = ad([1.0, 1.0], [0.5, 500.0], [0.0, 0.0], [0.0, 0.0], 1)
assert all(abs(x - 0.999) < 1e-9 for x in th), f"First step should be ≈ lr for both weights (bias correction + square root), got {th!r}."
assert abs(m[0] - 0.05) < 1e-12 and abs(v[0] - 0.00025) < 1e-12, f"m = 0.05, v = 0.00025 (store the raw, uncorrected moments), got {m[0]!r}, {v[0]!r}."
th, m, v = ad([2.0], [0.0], [0.0], [0.0], 1)
assert th == [2.0], "Zero gradient from the start: no move, no NaN (use eps)."
th, m, v = ad([0.0], [-3.0], [0.0], [0.0], 1, lr=0.01)
assert abs(th[0] - 0.01) < 1e-9, "Negative gradient → move up by lr."
w, m, v = [5.0], [0.0], [0.0]
for t in range(1, 3001):
    w, m, v = ad(w, [2 * (w[0] - 3)], m, v, t, lr=0.01)
assert abs(w[0] - 3) < 0.05, f"Adam should find the minimum of (w − 3)², got {w!r}."
