import math
H, CE, KL = ns.get("entropy"), ns.get("cross_entropy"), ns.get("kl")
assert H and CE and KL, "Keep entropy, cross_entropy and kl."
assert abs(H([0.25] * 4) - math.log(4)) < 1e-9, f"entropy of 4 equal outcomes returned {H([0.25] * 4)!r}, expected log 4 ≈ 1.386."
try:
    got = H([1.0, 0.0])
except ValueError:
    raise AssertionError("entropy([1, 0]) crashed on log(0). Skip terms where p is 0.")
assert abs(got) < 1e-12, f"entropy([1, 0]) returned {got!r}, expected 0: a certain outcome has no uncertainty."
assert abs(CE([0, 1], [0.5, 0.5]) - math.log(2)) < 1e-9, f"cross_entropy([0, 1], [0.5, 0.5]) returned {CE([0, 1], [0.5, 0.5])!r}, expected log 2."
p, q = [0.5, 0.3, 0.2], [0.4, 0.4, 0.2]
want = sum(a * math.log(a / b) for a, b in zip(p, q))
assert abs(KL(p, q) - want) < 1e-9, f"kl({p}, {q}) returned {KL(p, q)!r}, expected {want:.6f}."
assert abs(KL(p, p)) < 1e-12, "KL of a distribution with itself should be 0."
assert abs(KL([0.9, 0.1], [0.5, 0.5]) - KL([0.5, 0.5], [0.9, 0.1])) > 0.1, "KL isn't symmetric: KL(p‖q) and KL(q‖p) differ. Check your argument order."
