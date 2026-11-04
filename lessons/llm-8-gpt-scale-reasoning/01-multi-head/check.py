sh, mh, ca = ns.get("split_heads"), ns.get("multi_head"), ns["causal_attention"]
assert sh and mh, "Keep split_heads and multi_head."
rows = [[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]]
got = sh(rows, 3)
assert got == [[[1, 2], [7, 8]], [[3, 4], [9, 10]], [[5, 6], [11, 12]]], f"split_heads(rows, 3) gave {got!r}."
Q = [[1.0, 0.0, 2.0, 0.0], [0.0, 1.0, 0.0, 3.0], [1.0, 1.0, 1.0, 1.0]]
K = [[0.5, 1.0, 1.0, 0.0], [1.0, 0.0, 0.0, 1.0], [0.0, 0.0, 1.0, 1.0]]
V = [[1.0, 0.0, 0.0, 1.0], [0.0, 2.0, 2.0, 0.0], [3.0, 3.0, 3.0, 3.0]]
one = mh(Q, K, V, 1)
ref = ca(Q, K, V)
assert len(one) == 3 and all(abs(a - b) < 1e-9 for r1, r2 in zip(one, ref) for a, b in zip(r1, r2)), "With 1 head, multi_head should equal causal_attention."
two = mh(Q, K, V, 2)
h0 = ca([r[:2] for r in Q], [r[:2] for r in K], [r[:2] for r in V])
h1 = ca([r[2:] for r in Q], [r[2:] for r in K], [r[2:] for r in V])
want = [a + b for a, b in zip(h0, h1)]
assert len(two) == 3 and all(len(r) == 4 for r in two), "Each output row should be as wide as the input (heads joined back together)."
assert all(abs(a - b) < 1e-9 for r1, r2 in zip(two, want) for a, b in zip(r1, r2)), "With 2 heads, run attention on each half separately and join the outputs in head order."
