km = ns.get("kmeans")
assert km, "Keep kmeans."
pts = [(0, 0), (0, 2), (10, 10), (10, 12)]
c, a = km(pts, [(1, 1), (9, 9)], 1)
assert a == [0, 0, 1, 1], f"Assignments after one round should be [0, 0, 1, 1], got {a!r}."
assert [tuple(x) for x in c] == [(0.0, 1.0), (10.0, 11.0)], f"Centers should move to the means (0, 1) and (10, 11), got {c!r}."
c, a = km(pts, [(0, 0), (100, 100)], 2)
assert a == [0, 0, 0, 0] and tuple(c[1]) == (100, 100), "A center with no points should stay where it is."
c, a = km([(0, 0), (4, 0), (5, 0), (6, 0)], [(0, 0), (1, 0)], 3)
assert a == [0, 1, 1, 1] and abs(c[1][0] - 5) < 1e-9, f"Run several rounds: expected assignments [0, 1, 1, 1] and center 2 at x=5, got {a!r}, {c!r}."
c, a = km([(1, 0)], [(0, 0), (2, 0)], 1)
assert a == [0], "On a tie, pick the lower index."
