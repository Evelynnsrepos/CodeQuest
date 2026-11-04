import math
lk, ll, bp, nl = ns.get("likelihood"), ns.get("log_likelihood"), ns.get("best_p"), ns.get("nll_per_token")
assert lk and ll and bp and nl, "Keep likelihood, log_likelihood, best_p and nll_per_token."
flips = [1] * 7 + [0] * 3
assert abs(lk(0.7, flips) - 0.7 ** 7 * 0.3 ** 3) < 1e-15, f"likelihood(0.7, …) ≈ 0.002224, got {lk(0.7, flips)!r}."
assert abs(ll(0.7, flips) - math.log(0.7 ** 7 * 0.3 ** 3)) < 1e-9, "log_likelihood = sum of logs."
big = [1] * 1000
assert abs(ll(0.1, big) - 1000 * math.log(0.1)) < 1e-6, "Sum the logs; multiplying first underflows to 0."
assert abs(bp(flips) - 0.7) < 1e-9, f"best_p should be 0.7, got {bp(flips)!r}."
assert abs(bp([1, 0, 0, 0]) - 0.25) < 1e-9, "1 head in 4 → 0.25."
assert abs(nl([0.5, 0.25]) - (math.log(2) + math.log(4)) / 2) < 1e-12, f"nll_per_token([0.5, 0.25]) ≈ 1.04, got {nl([0.5, 0.25])!r}."
assert nl([1.0, 1.0]) == 0, "Perfectly confident and right: loss 0."
