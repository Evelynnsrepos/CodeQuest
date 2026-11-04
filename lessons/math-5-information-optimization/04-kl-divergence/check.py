import math
kl_, kv = ns.get("kl"), ns.get("kl_via_entropy")
assert kl_ and kv, "Keep kl and kl_via_entropy."
assert abs(kl_([0.5, 0.5], [0.9, 0.1]) - 0.5108256238) < 1e-9, f"KL(fair ‖ 90/10) ≈ 0.511, got {kl_([0.5, 0.5], [0.9, 0.1])!r}."
assert abs(kl_([0.9, 0.1], [0.5, 0.5]) - 0.3680642072) < 1e-9, "KL(90/10 ‖ fair) ≈ 0.368: order matters."
assert abs(kl_([0.2, 0.3, 0.5], [0.2, 0.3, 0.5])) < 1e-12, "KL(p ‖ p) = 0."
assert abs(kl_([1, 0], [0.7, 0.3]) + math.log(0.7)) < 1e-12, "Skip p = 0; one-hot KL = cross-entropy."
for p, q in [([0.5, 0.5], [0.9, 0.1]), ([0.1, 0.6, 0.3], [0.3, 0.3, 0.4])]:
    assert abs(kv(p, q) - kl_(p, q)) < 1e-12, "kl_via_entropy must equal kl."
    assert kl_(p, q) >= 0, "KL is never negative."
