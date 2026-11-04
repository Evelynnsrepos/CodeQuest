cv, mp = ns.get("conv2d"), ns.get("max_pool")
assert cv and mp, "Keep conv2d and max_pool."
img = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
got = cv(img, [[1, 0], [0, 1]])
assert got == [[6, 8], [12, 14]], f"conv2d with [[1,0],[0,1]] should be [[6, 8], [12, 14]], got {got!r}."
got = cv([[1, 2, 3, 4]], [[1, -1]])
assert got == [[-1, -1, -1]], f"A 1×4 image with a 1×2 kernel gives a 1×3 map: [[-1, -1, -1]], got {got!r}."
got = cv(img, [[1, 1, 1], [1, 1, 1], [1, 1, 1]])
assert got == [[45]], "A 3×3 kernel on a 3×3 image gives one number."
got = mp([[1, 2, 5, 6], [3, 4, 7, 8], [9, 1, 0, 0], [1, 1, 0, 2]], 2)
assert got == [[4, 8], [9, 2]], f"max_pool(…, 2) should be [[4, 8], [9, 2]], got {got!r}."
