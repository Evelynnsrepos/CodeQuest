pc, sl, sg, hv, ii = (ns.get(n) for n in ("percent_change", "slope", "sigma", "halvings", "in_interval"))
assert all((pc, sl, sg, hv, ii)), "Keep all five functions."
assert abs(pc(2.0, 1.5) + 25) < 1e-9 and abs(pc(80, 100) - 25) < 1e-9, "1. percent_change: (new − old) / old · 100."
assert sl((0, 3), (2, 7)) == 2 and sl((1, 5), (3, 1)) == -2, "2. slope: (y₂ − y₁) / (x₂ − x₁)."
assert sg(lambda i: i ** 2, 1, 3) == 14 and sg(lambda i: 1, 5, 5) == 1, "3. sigma: from a to b, both included."
assert hv(1000) == 10 and hv(8) == 3 and hv(1) == 0, "4. halvings: log₂ n rounded up."
assert ii(1, 0, 1, True, False) is False and ii(0, 0, 1, True, False) is True and ii(1, 0, 1, True, True) is True and ii(0.5, 0, 1, False, False) is True, "5. in_interval: [ hugs its number, ( keeps it out."
