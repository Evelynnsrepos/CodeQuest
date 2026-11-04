ex, ef, er = ns.get("expected"), ns.get("expected_f"), ns.get("expected_reward")
assert ex and ef and er, "Keep expected, expected_f and expected_reward."
die = {k: 1 / 6 for k in range(1, 7)}
assert abs(ex(die) - 3.5) < 1e-12, f"Die: 3.5, got {ex(die)!r}."
assert abs(ex({998: 0.001, -2: 0.999}) + 1) < 1e-12, "Lottery: −1 € per ticket (weight by probability!)."
assert abs(ef(die, lambda x: x * x) - 91 / 6) < 1e-12, f"E[X²] for a die is 91/6 ≈ 15.17, got {ef(die, lambda x: x * x)!r}."
assert abs(er({"a": 0.7, "b": 0.3}, {"a": 1, "b": 0}) - 0.7) < 1e-12, "Expected reward 0.7."
assert abs(er({"x": 0.2, "y": 0.5, "z": 0.3}, {"x": 2, "y": -1, "z": 0}) + 0.1) < 1e-12, "0.4 − 0.5 + 0 = −0.1."
