import math
sa, pr, cs, rs, gs = (ns.get(n) for n in ("slope_at", "power_rule", "chain_square", "relu_slope", "gd_step"))
assert all((sa, pr, cs, rs, gs)), "Keep all five functions."
assert abs(sa(lambda x: x ** 3, 2) - 12) < 1e-4 and abs(sa(math.exp, 0) - 1) < 1e-6, "1. slope_at: central difference with h = 1e-5."
assert pr(5, 3, 2) == 60 and pr(1, 1, 7) == 1, "2. power_rule: c · n · x^(n − 1)."
assert cs(3, 1, 1) == 24 and cs(1, -2, 2) == 0, "3. chain_square: 2 · (a·x + b) · a."
assert rs(3) == 1 and rs(-2) == 0 and rs(0) == 0, "4. relu_slope: 1 above 0, else 0."
assert abs(gs(0, -6, 0.1) - 0.6) < 1e-12 and gs(5, 2, 0.5) == 4, "5. gd_step: w − η · slope."
