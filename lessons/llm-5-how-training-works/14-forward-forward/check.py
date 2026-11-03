import math
g, sp, fl, nm = ns.get("goodness"), ns.get("softplus"), ns.get("ff_loss"), ns.get("normalize")
assert g and sp and fl and nm, "Keep goodness, softplus, ff_loss and normalize."
assert g([1.0, -2.0, 3.0]) == 14, f"goodness([1, −2, 3]) returned {g([1.0, -2.0, 3.0])!r}, expected 14."
assert abs(sp(0) - math.log(2)) < 1e-12, f"softplus(0) returned {sp(0)!r}, expected log 2."
try:
    big = sp(1000)
except OverflowError:
    raise AssertionError("softplus(1000) overflowed. Return x itself when x > 30.")
assert big == 1000, f"softplus(1000) returned {big!r}, expected 1000."
want = math.log(1 + math.exp(2 - 5)) + math.log(1 + math.exp(1 - 2))
assert abs(fl([1.0, 2.0], [1.0, 0.0], 2.0) - want) < 1e-12, f"ff_loss([1, 2], [1, 0], 2) returned {fl([1.0, 2.0], [1.0, 0.0], 2.0)!r}, expected {want:.6f}: softplus(θ − G_pos) + softplus(G_neg − θ)."
assert fl([3.0], [0.0], 2.0) < fl([0.0], [3.0], 2.0), "A layer that gives positives high goodness and negatives low goodness should have the lower loss."
n = nm([3.0, 4.0])
assert abs(n[0] - 0.6) < 1e-12 and abs(n[1] - 0.8) < 1e-12, f"normalize([3, 4]) returned {n!r}, expected [0.6, 0.8]."
assert nm([0.0, 0.0]) == [0.0, 0.0], "normalize of a zero vector should return it unchanged."
