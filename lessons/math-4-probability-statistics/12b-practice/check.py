al, ba, ex, zz, se = (ns.get(n) for n in ("at_least_once", "bayes", "expected", "z", "standard_error"))
assert all((al, ba, ex, zz, se)), "Keep all five functions."
assert abs(al(0.05, 20) - 0.6415) < 1e-4 and al(0.5, 1) == 0.5, "1. at_least_once: 1 − (1 − p)ⁿ."
assert abs(ba(0.01, 0.9, 0.05) - 0.1538) < 1e-4, "2. bayes: 0.009 / (0.009 + 0.0495) ≈ 0.154."
assert abs(ex([10, -2], [0.2, 0.8]) - 0.4) < 1e-12, "3. expected: Σ x · p."
assert zz(185, 170, 10) == 1.5 and zz(160, 170, 10) == -1, "4. z: (x − μ) / σ."
assert abs(se(2, 100) - 0.2) < 1e-12, "5. standard_error: σ / √n."
