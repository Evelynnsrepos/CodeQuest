bp, pv, sg = ns.get("binom_pmf"), ns.get("p_value_at_least"), ns.get("significant")
assert bp and pv and sg, "Keep binom_pmf, p_value_at_least and significant."
assert abs(bp(15, 20, 0.5) - 15504 / 2 ** 20) < 1e-15, f"binom_pmf(15, 20, 0.5) ≈ 0.0148, got {bp(15, 20, 0.5)!r}."
assert abs(sum(bp(k, 10, 0.3) for k in range(11)) - 1) < 1e-12, "All outcomes add to 1."
assert abs(pv(15, 20, 0.5) - 0.0206947327) < 1e-9, f"P(≥ 15 of 20) ≈ 0.0207, got {pv(15, 20, 0.5)!r}."
assert abs(pv(60, 100, 0.5) - 0.0284439668) < 1e-9, f"P(≥ 60 of 100) ≈ 0.0284, got {pv(60, 100, 0.5)!r}."
assert pv(0, 7, 0.3) > 0.999999, "P(≥ 0) is 1."
assert sg(0.028) is True and sg(0.06) is False and sg(0.04, alpha=0.01) is False, "significant: p < alpha."
