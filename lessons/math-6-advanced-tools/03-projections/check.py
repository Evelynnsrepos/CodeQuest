pr, rj, rd, dot = ns.get("project"), ns.get("reject"), ns.get("remove_direction"), ns.get("dot")
assert pr and rj and rd and dot, "Keep dot, project, reject and remove_direction."
close = lambda u, v: all(abs(x - y) < 1e-9 for x, y in zip(u, v))
assert close(pr([3, 4], [2, 0]), [3, 0]), "project([3,4], [2,0]) = (3, 0)."
assert close(pr([1, 2, 3], [1, 1, 1]), [2, 2, 2]), "project onto (1,1,1): (6/3)·(1,1,1) = (2,2,2)."
r = rj([1, 2, 3], [1, 1, 1])
assert close(r, [-1, 0, 1]) and abs(dot(r, [1, 1, 1])) < 1e-12, "reject: the leftover is perpendicular."
vs = rd([[3, 4], [1, 1]], [0, 5])
assert close(vs[0], [3, 0]) and close(vs[1], [1, 0]), "remove_direction: subtract each vector's projection onto d."
