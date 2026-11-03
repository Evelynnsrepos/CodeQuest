h, mg = ns.get("human"), ns.get("model_gb")
assert h and mg, "Keep human and model_gb."
for n, want in [(8e9, "8.0B"), (1.5e13, "15.0T"), (124_439_808, "124.4M"), (3500, "3.5K"), (1e6, "1.0M")]:
    assert h(n) == want, f"human({n!r}) should be {want!r}, got {h(n)!r}."
assert h(42) == "42", "Below 1000, just str(n)."
assert abs(mg(8e9, 2) - 16) < 1e-9 and abs(mg(7e9, 0.5) - 3.5) < 1e-9, f"model_gb(8e9, 2) should be 16, got {mg(8e9, 2)!r}."
