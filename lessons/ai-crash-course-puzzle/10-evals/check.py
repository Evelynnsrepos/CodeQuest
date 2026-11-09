ac, wi, ib = ns.get("accuracy"), ns.get("win_interval"), ns.get("is_better")
assert ac and wi and ib, "Keep accuracy, win_interval and is_better."
assert abs(ac(["Paris", "berlin ", "Rome"], ["paris", "Berlin", "Madrid"]) - 2 / 3) < 1e-12, "accuracy: compare stripped, lowercased."
lo, hi = wi(60, 100)
assert abs(lo - 0.50202) < 1e-4 and abs(hi - 0.69798) < 1e-4, f"60 of 100: about 0.502 to 0.698, got {(lo, hi)!r}."
assert ib(60, 100) and not ib(6, 10) and ib(700, 1000), "is_better only when the whole interval is above 0.5."
