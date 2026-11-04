mv, r9 = ns.get("matvec"), ns.get("rotate90")
assert mv and r9, "Keep matvec and rotate90."
assert mv([[1, 2], [3, 4]], [5, 6]) == [17, 39], f"matvec should give [17, 39], got {mv([[1, 2], [3, 4]], [5, 6])!r}."
assert mv([[1, 0, 2], [0, 1, 0]], [3, 4, 5]) == [13, 4], "A 2×3 matrix times a 3-vector gives a 2-vector."
try:
    mv([[1, 2], [3, 4]], [1, 2, 3])
except ValueError:
    pass
else:
    raise AssertionError("matvec should raise ValueError when shapes don't match.")
assert r9([1, 0]) == [0, 1] and r9([0, 1]) == [-1, 0] and r9([2, 3]) == [-3, 2], f"rotate90([1, 0]) should be [0, 1], got {r9([1, 0])!r}."
