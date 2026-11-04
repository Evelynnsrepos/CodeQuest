mf, tf, td = ns.get("matmul_flops"), ns.get("training_flops"), ns.get("training_days")
assert mf and tf and td, "Keep matmul_flops, training_flops and training_days."
assert mf(2, 3, 4) == 48, f"matmul_flops(2, 3, 4) returned {mf(2, 3, 4)!r}, expected 2 × 2 × 3 × 4 = 48."
assert tf(1e9, 20e9) == 1.2e20, f"training_flops(1e9, 20e9) returned {tf(1e9, 20e9)!r}, expected 6 × 1e9 × 20e9 = 1.2e20."
got = td(86400e12, 1, 1.0)
assert abs(got - 1) < 1e-9, f"training_days(86400e12, 1, 1.0) returned {got!r}, expected 1 day."
got = td(86400e12, 2, 0.5)
assert abs(got - 1) < 1e-9, f"training_days(86400e12, 2, 0.5) returned {got!r}, expected 1 day (2 TFLOPS at 50%)."
