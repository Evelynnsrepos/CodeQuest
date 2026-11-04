import math
sm, ce = ns.get("softmax"), ns.get("cross_entropy")
assert sm and ce, "Keep softmax and cross_entropy."
p = sm([1.0, 1.0])
assert all(abs(a - 0.5) < 1e-12 for a in p), f"Two equal scores give [0.5, 0.5], got {p!r}."
p = sm([2.0, 1.0, 0.1])
e = [math.exp(2), math.exp(1), math.exp(0.1)]
assert all(abs(a - b / sum(e)) < 1e-12 for a, b in zip(p, e)), "softmax should be e^(z_i) / Σ_j e^(z_j)."
assert abs(sum(p) - 1) < 1e-12, "The outputs should sum to 1."
assert abs(ce([2.0, 1.0, 0.1], 0) - (-math.log(e[0] / sum(e)))) < 1e-12, "cross_entropy is −log of softmax(z)[t]."
assert abs(ce([0.0, 0.0, 0.0, 0.0], 3) - math.log(4)) < 1e-12, "With 4 equal scores the loss is ln 4."
