tp, by = ns.get("total_prob"), ns.get("bayes")
assert tp and by, "Keep total_prob and bayes."
assert abs(tp(0.9, 0.01, 0.09) - 0.0981) < 1e-12, f"P(+) = 0.0981, got {tp(0.9, 0.01, 0.09)!r}."
assert abs(by(0.9, 0.01, 0.09) - 0.0917431193) < 1e-9, f"P(sick | +) ≈ 0.0917, got {by(0.9, 0.01, 0.09)!r}."
assert abs(by(0.99, 0.5, 0.01) - 0.99) < 1e-12, "With a 50% prior and a symmetric 99% test: 0.99."
assert abs(by(0.6, 0.4, 0.2) - 0.24 / 0.36) < 1e-12, "bayes(0.6, 0.4, 0.2) = 0.24 / 0.36."
