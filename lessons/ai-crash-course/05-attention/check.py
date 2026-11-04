w, at = ns.get("weights"), ns.get("attend")
assert w and at, "Keep weights and attend."
ws = w([0.0, 2.6, 0.0, 1.4])
assert abs(sum(ws) - 1) < 1e-9 and max(range(4), key=lambda i: ws[i]) == 1, "weights: softmax, the biggest score gets the biggest weight."
out = at([0.0, 0.0], [[2, 0], [0, 4]])
assert all(abs(a - b) < 1e-9 for a, b in zip(out, [1, 2])), f"Equal scores → plain average [1, 2], got {out!r}."
out = at([10.0, -10.0], [[1, 1], [9, 9]])
assert abs(out[0] - 1) < 1e-6, "One huge score → that token's value."
