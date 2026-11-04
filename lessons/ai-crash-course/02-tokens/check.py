et, co = ns.get("estimate_tokens"), ns.get("cost")
assert et and co, "Keep estimate_tokens and cost."
assert et("unbelievable") == 3 and et("hello") == 2 and et("") == 0, "estimate_tokens: len / 4, rounded up."
assert abs(co(20_000, 1_000, 3, 15) - 0.075) < 1e-12, "20,000 × 3 + 1,000 × 15 = 75,000 → 0.075 dollars."
assert abs(co(1_000_000, 0, 0.5, 2) - 0.5) < 1e-12, "Prices are per million tokens."
