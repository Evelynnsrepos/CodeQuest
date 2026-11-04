import math
cf, cg = ns.get("ce_from_logits"), ns.get("ce_grad")
assert cf and cg, "Keep ce_from_logits and ce_grad."
assert abs(cf([2, 1, 0], 0) + math.log(0.6652409558)) < 1e-9, f"ce_from_logits([2, 1, 0], 0) ≈ 0.408, got {cf([2, 1, 0], 0)!r}."
g = cg([2, 1, 0], 0)
assert all(abs(a - b) < 1e-9 for a, b in zip(g, [-0.3347590442, 0.2447284711, 0.0900305732])), f"ce_grad([2, 1, 0], 0) ≈ [−0.335, 0.245, 0.090], got {g!r}."
assert abs(sum(g)) < 1e-12, "The gradient entries sum to 0."
z, t = [0.3, -1.2, 2.0, 0.5], 1
g = cg(z, t)
for i in range(len(z)):
    up, dn = list(z), list(z)
    up[i] += 1e-6
    dn[i] -= 1e-6
    num = (cf(up, t) - cf(dn, t)) / 2e-6
    assert abs(g[i] - num) < 1e-6, f"Gradient check failed for logit {i}: yours {g[i]}, numeric {num}."
