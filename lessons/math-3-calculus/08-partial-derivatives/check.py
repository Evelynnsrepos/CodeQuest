pa, lp = ns.get("partial"), ns.get("loss_partials")
assert pa and lp, "Keep partial and loss_partials."
L = lambda w, b: (w * 2 + b - 7) ** 2
assert abs(pa(L, [1, 1], 0) + 16) < 1e-5 and abs(pa(L, [1, 1], 1) + 8) < 1e-5, f"Partials at (1, 1) should be -16 and -8, got {pa(L, [1, 1], 0)!r}, {pa(L, [1, 1], 1)!r}."
f = lambda x, y, z: x * y + z ** 2
assert abs(pa(f, [2, 3, 4], 0) - 3) < 1e-5 and abs(pa(f, [2, 3, 4], 2) - 8) < 1e-5, "∂/∂x of xy + z² is y; ∂/∂z is 2z."
pt = [2, 3, 4]
pa(f, pt, 0)
assert pt == [2, 3, 4], "Don't change the caller's point list (copy it)."
assert lp(1, 1, 2, 7) == (-16, -8), f"loss_partials(1, 1, 2, 7) should be (-16, -8), got {lp(1, 1, 2, 7)!r}."
dw, db = lp(0.5, -1, 3, 0)
assert abs(dw - 3) < 1e-12 and abs(db - 1) < 1e-12, "error 0.5 → (2·0.5·3, 2·0.5) = (3, 1)."
