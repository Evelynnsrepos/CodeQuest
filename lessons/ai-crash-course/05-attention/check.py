w, at = ns.get("weights"), ns.get("attend")
assert w and at, "Keep weights and attend."
ws = w([0.0, 2.6, 0.0, 1.4])
assert abs(sum(ws) - 1) < 1e-9 and max(range(4), key=lambda i: ws[i]) == 1, f"weights: softmax. They add up to 1 and the biggest score gets the biggest weight. Got {ws!r}."
assert abs(w([1000.0, 1000.0])[0] - 0.5) < 1e-9, "weights: subtract the biggest score first, or e to the 1000 is too big."
out = at([0.0, 0.0], [[2, 0], [0, 4]])
assert all(abs(a - b) < 1e-9 for a, b in zip(out, [1, 2])) and len(out) == 2, f"Equal scores → plain average [1, 2], got {out!r}."
out = at([10.0, -10.0], [[1, 1], [9, 9]])
assert abs(out[0] - 1) < 1e-6 and abs(out[1] - 1) < 1e-6, "One huge score → (almost exactly) that token's vector."
