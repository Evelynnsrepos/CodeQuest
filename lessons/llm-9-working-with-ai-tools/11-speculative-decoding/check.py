et, sp, bk = ns.get("expected_tokens"), ns.get("speedup"), ns.get("best_k")
assert et and sp and bk, "Keep expected_tokens, speedup and best_k."
assert abs(et(0.8, 4) - 3.36160) < 1e-9, f"expected_tokens(0.8, 4) ≈ 3.36, got {et(0.8, 4)!r}."
assert abs(et(0.5, 4) - 1.9375) < 1e-12 and et(1, 4) == 5 and abs(et(0, 4) - 1) < 1e-12, "α = 0.5 → 1.94; α = 1 → k + 1; α = 0 → 1."
assert abs(sp(0.8, 4, 0.05) - 2.8013333) < 1e-6, f"speedup(0.8, 4, 0.05) ≈ 2.80, got {sp(0.8, 4, 0.05)!r}."
k = bk(0.8, 0.05)
assert all(sp(0.8, k, 0.05) >= sp(0.8, j, 0.05) for j in range(1, 17)) and 1 <= k <= 16, "best_k must be the argmax."
assert bk(0.95, 0.01) > bk(0.6, 0.01), "Higher acceptance → longer drafts pay off."
