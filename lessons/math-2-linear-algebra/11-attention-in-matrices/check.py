import math
cmk, at = ns.get("causal_mask"), ns.get("attention")
assert cmk and at, "Keep causal_mask and attention."
inf = float("-inf")
assert cmk(3) == [[0.0, inf, inf], [0.0, 0.0, inf], [0.0, 0.0, 0.0]], f"causal_mask(3) is wrong: {cmk(3)!r}."
Q = [[1.0, 0.0], [0.0, 2.0]]
K = [[2.0, 0.0], [0.0, 1.0]]
V = [[1.0, 0.0], [0.0, 1.0]]
out = at(Q, K, V, True)
assert abs(out[0][0] - 1) < 1e-12 and abs(out[0][1]) < 1e-12, f"With the mask, token 1 only sees itself: row 1 should be V[0] = [1, 0], got {out[0]!r}."
s = [0 / math.sqrt(2), 2 / math.sqrt(2)]
w = [math.exp(s[0]) / (math.exp(s[0]) + math.exp(s[1])), math.exp(s[1]) / (math.exp(s[0]) + math.exp(s[1]))]
assert all(abs(a - b) < 1e-9 for a, b in zip(out[1], w)), f"Row 2 should be softmax([0, 2] / √2) mixing V: {w!r}, got {out[1]!r}. Did you divide by √d?"
full = at(Q, K, V, False)
s0 = [2 / math.sqrt(2), 0.0]
w0 = math.exp(s0[0]) / (math.exp(s0[0]) + 1)
assert abs(full[0][0] - w0) < 1e-9, "Without the mask, token 1 can also see token 2."
