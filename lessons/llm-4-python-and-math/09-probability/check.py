ev, var, s = ns.get("expected_value"), ns.get("variance"), ns.get("sample")
assert ev and var and s, "Keep expected_value, variance and sample."
assert abs(ev([0, 10], [0.7, 0.3]) - 3) < 1e-9, f"expected_value([0, 10], [0.7, 0.3]) returned {ev([0, 10], [0.7, 0.3])!r}, expected 3."
assert abs(var([0, 10], [0.7, 0.3]) - 21) < 1e-9, f"variance([0, 10], [0.7, 0.3]) returned {var([0, 10], [0.7, 0.3])!r}, expected 0.7·9 + 0.3·49 = 21."
assert abs(var([5], [1.0])) < 1e-12, "A distribution with one certain outcome has variance 0."
p = [0.5, 0.3, 0.2]
for r, want in [(0.0, 0), (0.49, 0), (0.5, 1), (0.79, 1), (0.8, 2), (0.999, 2)]:
    assert s(p, r) == want, f"sample([0.5, 0.3, 0.2], {r}) returned {s(p, r)!r}, expected {want}."
assert s([0.3333333, 0.3333333, 0.3333333], 0.99999999) == 2, "When rounding makes the probabilities add up to slightly less than 1, return the last index."
