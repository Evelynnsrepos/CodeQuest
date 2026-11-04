ro, mo, bl = ns.get("route"), ns.get("moe_output"), ns.get("balance_loss")
assert ro and mo and bl, "Keep route, moe_output and balance_loss."
r = ro([2, 1, 0.5, -1], 2)
assert [i for i, _ in r] == [0, 1] and abs(r[0][1] - 0.7310585786) < 1e-9 and abs(r[1][1] - 0.2689414214) < 1e-9, f"route should be [(0, 0.731), (1, 0.269)], got {r!r}."
r = ro([0.1, 3, -2, 2.5], 3)
assert [i for i, _ in r] == [1, 3, 0] and abs(sum(g for _, g in r) - 1) < 1e-12, "Top 3, weights add to 1 (softmax over the kept scores only)."
outs = [[1, 0], [0, 1], [5, 5], [9, 9]]
y = mo([2, 1, 0.5, -1], 2, outs)
assert abs(y[0] - 0.7310585786) < 1e-9 and abs(y[1] - 0.2689414214) < 1e-9, f"Mix only the chosen experts, got {y!r}."
assert abs(bl([0.25] * 4, [0.25] * 4) - 1) < 1e-12, "Balanced: 1."
assert abs(bl([0.5, 0.3, 0.1, 0.1], [0.4, 0.3, 0.2, 0.1]) - 1.28) < 1e-12, "Skewed: 1.28."
assert abs(bl([1, 0, 0, 0], [1, 0, 0, 0], alpha=0.01) - 0.04) < 1e-12, "Collapsed: 4, times alpha."
