inf, cl = ns.get("info_nce"), ns.get("clip_loss")
assert inf and cl, "Keep info_nce and clip_loss."
assert abs(inf([0.9, 0.1, 0.2], 0, 1.0) - 0.6657319272) < 1e-9, f"τ = 1: ≈ 0.666, got {inf([0.9, 0.1, 0.2], 0, 1.0)!r}."
assert abs(inf([0.9, 0.1, 0.2], 0, 0.1) - 0.0012465673) < 1e-9, f"τ = 0.1: ≈ 0.00125, got {inf([0.9, 0.1, 0.2], 0, 0.1)!r}."
assert inf([0.9, 0.1, 0.2], 1, 0.1) > 5, "If the positive is a bad match, the loss is large."
try:
    v = inf([1.0, 0.5], 0, 0.001)
except OverflowError:
    raise AssertionError("Overflow at tiny τ: use the max-shift trick from lesson 06.")
assert abs(v - (1 + __import__("math").exp(-500))) < 2 and v >= 0, "Tiny τ must not overflow."
assert abs(cl([[0.9, 0.1], [0.2, 0.8]], 0.1) - 0.0011585061) < 1e-9, f"clip_loss ≈ 0.00116, got {cl([[0.9, 0.1], [0.2, 0.8]], 0.1)!r}."
