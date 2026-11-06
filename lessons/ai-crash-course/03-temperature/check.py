sm = ns.get("softmax_t")
assert sm, "Keep softmax_t."
p = sm([2.0, 1.0, 0.1], 1)
assert all(abs(a - b) < 1e-3 for a, b in zip(p, [0.659, 0.242, 0.099])), f"T = 1: about [0.66, 0.24, 0.10], got {p!r}."
assert abs(sum(sm([3, 1, 2], 0.5)) - 1) < 1e-9, "The probabilities must add up to 1 (step 4: divide by the total)."
assert sm([2.0, 1.0, 0.1], 0.2)[0] > 0.99, "Low temperature: the top token gets almost everything. Did you divide by t in step 1?"
assert sm([2.0, 1.0, 0.1], 5)[0] < 0.42, "High temperature: flatter. Did you divide by t in step 1?"
p = sm([1000, 999], 1)
assert abs(p[0] - 0.7311) < 1e-3, "Subtract the biggest score first (step 2 and 3), or e to the 1000 is too big."
