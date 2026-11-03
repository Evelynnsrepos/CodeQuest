ad, sc, lc = ns.get("add"), ns.get("scale"), ns.get("lin_comb")
assert ad and sc and lc, "Keep add, scale and lin_comb."
assert ad([3, 1], [1, 2]) == [4, 3], f"add([3, 1], [1, 2]) should be [4, 3], got {ad([3, 1], [1, 2])!r}. (List + list glues them!)"
assert sc(2, [3, 1]) == [6, 2] and sc(-1, [1, -2]) == [-1, 2], f"scale(2, [3, 1]) should be [6, 2], got {sc(2, [3, 1])!r}."
assert lc([0.5, 2], [[2, 4], [1, -1]]) == [3, 0], f"lin_comb should give [3, 0], got {lc([0.5, 2], [[2, 4], [1, -1]])!r}."
assert lc([1, 1, 1], [[1, 0], [0, 1], [1, 1]]) == [2, 2], "Three vectors: [1,0] + [0,1] + [1,1] = [2, 2]."
