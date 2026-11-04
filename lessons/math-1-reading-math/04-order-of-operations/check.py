p, q, r = ns.get("p"), ns.get("q"), ns.get("r")
assert p and q and r, "Keep p, q and r."
assert abs(p(3) - 16 / 6) < 1e-12, f"p(3) should be (3+1)² / (2·3) = 2.667, got {p(3)!r}. Put brackets around the top AND the bottom."
assert abs(p(1) - 2.0) < 1e-12, "p(1) should be 4 / 2 = 2."
assert abs(q(5, 3) - 0.25) < 1e-12, f"q(5, 3) should be (5−3)/(5+3) = 0.25, got {q(5, 3)!r}."
assert r(2) == 9 and r(0) == 1, f"r(2) should be 3·4 − 4 + 1 = 9, got {r(2)!r}. The square applies to x only."
