d, c = ns.get("dot"), ns.get("cosine")
assert d and c, "Keep the functions dot and cosine."
got = d([1, 2, 3], [4, 5, 6])
assert got == 32, f"dot([1, 2, 3], [4, 5, 6]) returned {got!r}, expected 32 (4 + 10 + 18)."
got = c([1, 0], [0, 1])
assert abs(got) < 1e-9, f"cosine([1, 0], [0, 1]) returned {got!r}, expected 0: the vectors are at a right angle."
got = c([1, 2], [2, 4])
assert abs(got - 1) < 1e-9, f"cosine([1, 2], [2, 4]) returned {got!r}, expected 1: same direction, different length."
got = c([1, 1], [-3, -3])
assert abs(got + 1) < 1e-9, f"cosine([1, 1], [-3, -3]) returned {got!r}, expected -1: opposite directions."
