d, m = ns.get("distance"), ns.get("mae")
assert d and m, "Keep distance and mae."
assert d(7, 10) == 3 and d(10, 7) == 3, f"distance(7, 10) and distance(10, 7) should both be 3, got {d(7, 10)!r} and {d(10, 7)!r}."
assert d(-2, 3) == 5, "From -2 to 3 is 5."
assert m([10, 10], [7, 13]) == 3, f"mae([10, 10], [7, 13]) should be 3 (not 0: use the absolute value), got {m([10, 10], [7, 13])!r}."
assert abs(m([1, 2, 3], [1, 0, 6]) - 5 / 3) < 1e-12, "mae([1,2,3], [1,0,6]) should be (0 + 2 + 3) / 3."
