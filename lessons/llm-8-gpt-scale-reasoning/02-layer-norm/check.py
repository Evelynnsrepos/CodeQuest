import math
ln, rn = ns.get("layer_norm"), ns.get("rms_norm")
assert ln and rn, "Keep layer_norm and rms_norm."
y = ln([1.0, 2.0, 3.0, 4.0], [1.0] * 4, [0.0] * 4)
assert abs(sum(y)) < 1e-6, f"After LayerNorm (gamma 1, beta 0) the mean should be 0, got {sum(y)/4:.4f}."
assert abs(sum(v * v for v in y) / 4 - 1) < 1e-4, "After LayerNorm the variance should be about 1. Divide by the population variance (/ d), not d - 1."
y = ln([1.0, 2.0, 3.0, 4.0], [2.0, 2.0, 2.0, 2.0], [1.0, 1.0, 1.0, 1.0])
want = [(v - 2.5) / math.sqrt(1.25 + 1e-5) * 2 + 1 for v in [1, 2, 3, 4]]
assert all(abs(a - b) < 1e-9 for a, b in zip(y, want)), "Apply gamma (multiply) and beta (add) after normalizing."
y = rn([3.0, 4.0], [1.0, 2.0])
r = math.sqrt(12.5 + 1e-5)
assert all(abs(a - b) < 1e-9 for a, b in zip(y, [3 / r, 8 / r])), f"rms_norm([3, 4], [1, 2]) should be [3/rms, 4/rms*2] with rms = sqrt(12.5 + eps), got {y!r}."
