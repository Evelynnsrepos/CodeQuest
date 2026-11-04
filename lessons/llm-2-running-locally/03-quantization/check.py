qz, dq = ns.get("quantize"), ns.get("dequantize")
assert qz and dq, "Keep the functions quantize and dequantize."
scale, qs = qz([0.7, -0.35, 0.1, 0.0])
assert abs(scale - 0.1) < 1e-9, f"quantize([0.7, -0.35, 0.1, 0.0]) gave scale {scale!r}, expected 0.7 / 7 = 0.1."
assert qs == [7, -4, 1, 0] or qs == [7, -3, 1, 0], f"quantize([0.7, -0.35, 0.1, 0.0]) gave {qs!r}, expected [7, -4, 1, 0] (-3.5 may round either way)."
scale, qs = qz([0.0, 0.0])
assert scale == 1.0 and qs == [0, 0], f"quantize([0, 0]) returned {(scale, qs)!r}, expected (1.0, [0, 0])."
assert all(-8 <= q <= 7 for q in qz([-1.0, 1.0, -0.99])[1]), "Every quantized value must be between -8 and 7."
got = dq(0.5, [2, -3])
assert got == [1.0, -1.5], f"dequantize(0.5, [2, -3]) returned {got!r}, expected [1.0, -1.5]."
assert ns.get("outlier_hurts") is True, "Look at the quantized outlier block: what happened to the small weights next to 6.5?"
