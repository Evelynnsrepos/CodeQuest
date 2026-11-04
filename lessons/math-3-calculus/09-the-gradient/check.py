gr, gm = ns.get("gradient"), ns.get("grad_mse")
assert gr and gm, "Keep gradient and grad_mse."
g = gr(lambda x, y: x * x + 3 * y, [1, 2])
assert len(g) == 2 and abs(g[0] - 2) < 1e-5 and abs(g[1] - 3) < 1e-5, f"∇(x² + 3y) at (1, 2) is (2, 3), got {g!r}."
g = gr(lambda a, b, c: a * b * c, [1, 2, 3])
assert len(g) == 3 and all(abs(u - v) < 1e-5 for u, v in zip(g, [6, 3, 2])), "∇(abc) at (1, 2, 3) is (6, 3, 2)."
assert gm(1, 1, [2], [7]) == (-16, -8), f"One point: same as lesson 08, got {gm(1, 1, [2], [7])!r}."
xs, ys = [1, 2, 3], [2, 4, 7]
L = lambda w, b: sum((w * x + b - y) ** 2 for x, y in zip(xs, ys)) / 3
dw, db = gm(0.5, 0.2, xs, ys)
assert abs(dw - gr(L, [0.5, 0.2])[0]) < 1e-5 and abs(db - gr(L, [0.5, 0.2])[1]) < 1e-5, "grad_mse should average over all points (match the numeric gradient)."
