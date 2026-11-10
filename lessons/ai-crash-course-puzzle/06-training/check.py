gr, tr = ns.get("gradient"), ns.get("train")
assert gr and tr, "Keep gradient and train."
assert abs(gr(0, [1, 2, 3], [2, 4, 6]) + 56 / 3) < 1e-9, f"gradient(0, [1, 2, 3], [2, 4, 6]) = (−4 − 16 − 36) ÷ 3 ≈ −18.67, yours gave {gr(0, [1, 2, 3], [2, 4, 6])!r}."
assert abs(gr(2, [1, 2, 3], [2, 4, 6])) < 1e-12 and abs(gr(1, [2], [0]) - 8) < 1e-12, "gradient: 0 at the right answer; for w = 1, x = 2, y = 0 it is 2 × 2 × 2 = 8."
assert abs(tr([1, 2, 3], [2, 4, 6], 1, 0.05) - 0.9333333) < 1e-6, "One step from 0: w = 0 − 0.05 × (−18.67) ≈ 0.933."
assert abs(tr([1, 2, 3], [2, 4, 6], 50, 0.05) - 2) < 1e-3 and abs(tr([1, 2], [-3, -6], 200, 0.05) + 3) < 1e-3, "The data is y = 2x: w should reach about 2 (and −3 for y = −3x)."
assert abs(tr([1, 2, 3], [2, 4, 6], 10, 0.5)) > 100, "With lr = 0.5 the steps overshoot and w explodes: that's a too-big learning rate."
