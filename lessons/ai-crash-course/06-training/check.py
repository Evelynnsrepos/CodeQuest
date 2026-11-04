tr = ns.get("train")
assert tr, "Keep train."
assert abs(tr([1, 2, 3], [2, 4, 6], 50, 0.05) - 2) < 1e-3, "The data is y = 2x: w should reach about 2."
assert abs(tr([1, 2, 3], [2, 4, 6], 1, 0.05) - 0.9333333) < 1e-6, "One step from 0: gradient = −56/3, so w = 0.05 · 56/3 ≈ 0.933."
assert abs(tr([1, 2], [-3, -6], 200, 0.05) + 3) < 1e-3, "Works for y = −3x too."
assert abs(tr([1, 2, 3], [2, 4, 6], 10, 0.5)) > 100, "With lr = 0.5 the steps overshoot and w explodes: that's a too-big learning rate."
