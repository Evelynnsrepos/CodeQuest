pa, po, pl, pl1 = ns.get("p_and"), ns.get("p_or"), ns.get("p_all"), ns.get("p_at_least_one")
assert pa and po and pl and pl1, "Keep p_and, p_or, p_all and p_at_least_one."
assert pa(0.5, 0.5) == 0.25, f"p_and(0.5, 0.5) = 0.25, got {pa(0.5, 0.5)!r}."
assert abs(po(13 / 52, 4 / 52, 1 / 52) - 16 / 52) < 1e-12, f"Heart or king = 16/52, got {po(13 / 52, 4 / 52, 1 / 52)!r}."
assert abs(pl(0.95, 20) - 0.3584859224) < 1e-9, f"p_all(0.95, 20) ≈ 0.358, got {pl(0.95, 20)!r}."
assert abs(pl1(0.05, 10) - 0.4012630608) < 1e-9, f"p_at_least_one(0.05, 10) ≈ 0.401, got {pl1(0.05, 10)!r}."
assert pl1(0.05, 30) < 1, "Must stay below 1 even for many tries."
assert pl1(0.3, 0) == 0, "Zero tries: never."
