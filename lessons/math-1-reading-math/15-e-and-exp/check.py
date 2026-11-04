import math
co, sg, dc = ns.get("compound"), ns.get("sigmoid"), ns.get("decay")
assert co and sg and dc, "Keep compound, sigmoid and decay."
assert co(1) == 2 and co(2) == 2.25, f"compound(2) should be 1.5² = 2.25, got {co(2)!r}."
assert abs(co(10 ** 6) - math.e) < 1e-5, "compound(1,000,000) should be very close to e."
assert sg(0) == 0.5, f"sigmoid(0) should be 0.5, got {sg(0)!r}."
assert abs(sg(2) - 1 / (1 + math.exp(-2))) < 1e-12 and sg(-10) < 0.001, "sigmoid(z) = 1 / (1 + e^(-z))."
assert abs(dc(100, 0.5, 2) - 100 / math.e) < 1e-9, f"decay(100, 0.5, 2) = 100·e^(-1) ≈ 36.79, got {dc(100, 0.5, 2)!r}."
