tps, log = ns.get("tokens_per_second"), ns.get("layers_on_gpu")
assert tps and log, "Keep the functions tokens_per_second and layers_on_gpu."
got = tps(4.0, 0, 400, 50)
assert abs(got - 100) < 1e-9, f"tokens_per_second(4.0, 0, 400, 50) returned {got!r}, expected 400 / 4 = 100."
got = tps(4.0, 1.0, 400, 50)
assert abs(got - 1 / (0.01 + 0.02)) < 1e-9, f"tokens_per_second(4.0, 1.0, 400, 50) returned {got!r}, expected 1 / (4/400 + 1/50) ≈ 33.3."
got = log(10.0, 40, 5.0)
assert got == 20, f"layers_on_gpu(10.0, 40, 5.0) returned {got!r}, expected 20 (each layer is 0.25 GB)."
got = log(4.9, 32, 11.0)
assert got == 32, f"layers_on_gpu(4.9, 32, 11.0) returned {got!r}, expected 32: the whole model fits, but there are only 32 layers."
got = log(14.3, 40, 0.2)
assert got == 0, f"layers_on_gpu(14.3, 40, 0.2) returned {got!r}, expected 0."
