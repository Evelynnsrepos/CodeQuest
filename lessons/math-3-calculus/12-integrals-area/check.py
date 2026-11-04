import math
ri, pb, au = ns.get("riemann"), ns.get("prob_between"), ns.get("auc")
assert ri and pb and au, "Keep riemann, prob_between and auc."
assert abs(ri(lambda x: 2 * x, 0, 3, 3) - 9) < 1e-12, f"2x from 0 to 3 with 3 strips: 9, got {ri(lambda x: 2 * x, 0, 3, 3)!r}."
assert abs(ri(lambda x: x * x, 0, 1, 2) - 0.3125) < 1e-12, "x² with 2 midpoint strips: 0.3125 (use the MIDDLE of each strip)."
assert abs(ri(lambda x: x * x, 0, 1, 1000) - 1 / 3) < 1e-6, "x² from 0 to 1 is 1/3."
assert abs(ri(lambda x: 2 * x, 3, 0, 3) + 9) < 1e-12, "Backwards gives a negative area."
normal = lambda x: math.exp(-x * x / 2) / math.sqrt(2 * math.pi)
assert abs(pb(normal, -1, 1) - 0.6827) < 1e-3, "About 68% of a normal distribution lies within 1 of the middle."
assert abs(au([(0, 0), (1, 1)]) - 0.5) < 1e-12, "The diagonal (coin flip) has AUC 0.5."
assert abs(au([(0, 0), (0, 1), (1, 1)]) - 1) < 1e-12, "A perfect classifier has AUC 1."
assert abs(au([(0, 0), (0.5, 0.8), (1, 1)]) - 0.65) < 1e-12, "0.5·0.8/2 + 0.5·1.8/2 = 0.65."
