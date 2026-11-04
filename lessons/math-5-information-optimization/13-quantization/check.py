qz, dq, me = ns.get("quantize"), ns.get("dequantize"), ns.get("max_error")
assert qz and dq and me, "Keep quantize, dequantize and max_error."
ws = [0.5, -1.27, 0.03]
qs, s = qz(ws, 8)
assert qs == [50, -127, 3] and abs(s - 0.01) < 1e-12, f"8-bit: ([50, -127, 3], 0.01), got {(qs, s)!r}."
qs, s = qz(ws, 4)
assert qs == [3, -7, 0] and abs(s - 1.27 / 7) < 1e-12, f"4-bit: ([3, -7, 0], 0.181), got {(qs, s)!r}."
assert all(abs(a - b) < 1e-12 for a, b in zip(dq([3, -7, 0], 1.27 / 7), [3 * 1.27 / 7, -1.27, 0])), "dequantize = q · scale."
assert abs(me(ws, 4) - (3 * 1.27 / 7 - 0.5)) < 1e-12, f"4-bit max error ≈ 0.044, got {me(ws, 4)!r}."
qs, s = qz(ws + [100], 8)
assert qs[2] == 0 and qs[3] == 127, "An outlier makes small weights collapse to 0."
assert me([0.2, -0.9, 0.33, 0.71], 8) <= 0.9 / 127 / 2 + 1e-12, "Error is at most half a step."
