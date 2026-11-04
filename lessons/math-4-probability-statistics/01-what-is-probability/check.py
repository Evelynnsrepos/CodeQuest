pr, co, iv = ns.get("prob"), ns.get("complement"), ns.get("is_valid")
assert pr and co and iv, "Keep prob, complement and is_valid."
assert abs(pr(1, 6) - 1 / 6) < 1e-12 and pr(3, 6) == 0.5, f"prob(1, 6) should be 1/6, got {pr(1, 6)!r}."
assert abs(co(0.92) - 0.08) < 1e-12 and co(0) == 1, f"complement(0.92) should be 0.08, got {co(0.92)!r}."
assert iv(0) and iv(1) and iv(0.3), "0, 1 and 0.3 are valid."
assert not iv(1.5) and not iv(-0.1), "1.5 and −0.1 are not probabilities."
