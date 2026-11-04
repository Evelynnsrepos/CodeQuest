tr, idn, sy = ns.get("transpose"), ns.get("identity"), ns.get("is_symmetric")
assert tr and idn and sy, "Keep transpose, identity and is_symmetric."
assert tr([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], f"Got {tr([[1, 2, 3], [4, 5, 6]])!r}."
assert tr([[1, 2, 3]]) == [[1], [2], [3]], "A row becomes a column."
assert idn(3) == [[1, 0, 0], [0, 1, 0], [0, 0, 1]] and idn(1) == [[1]], f"identity(3) is wrong: {idn(3)!r}."
assert sy([[1, 7], [7, 2]]) is True and sy([[1, 2], [3, 4]]) is False, "is_symmetric: A equals its transpose."
