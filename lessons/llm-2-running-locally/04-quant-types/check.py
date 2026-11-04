fs, bq = ns.get("file_size_gb"), ns.get("best_quant")
assert fs and bq, "Keep the functions file_size_gb and best_quant."
got = fs(8, "Q4_K_M")
assert abs(got - 4.8) < 1e-9, f"file_size_gb(8, 'Q4_K_M') returned {got!r}, expected 8 × 4.8 / 8 = 4.8."
got = fs(10, "Q8_0")
assert abs(got - 10.625) < 1e-9, f"file_size_gb(10, 'Q8_0') returned {got!r}, expected 10.625."
cases = [((8, 10), "Q8_0"), ((14, 10), "Q5_K_M"), ((24, 10), "Q2_K"), ((24, 12), "Q3_K_M"), ((32, 12), "Q2_K"), ((32, 10), None), ((1, 10), "F16")]
for args, want in cases:
    got = bq(*args)
    assert got == want, f"best_quant{args} returned {got!r}, expected {want!r}."
