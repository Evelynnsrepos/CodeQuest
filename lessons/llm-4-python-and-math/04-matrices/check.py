sh, tr, mm = ns.get("shape"), ns.get("transpose"), ns.get("matmul")
assert sh and tr and mm, "Keep shape, transpose and matmul."
assert sh([[1, 2, 3]]) == (1, 3), f"shape([[1, 2, 3]]) returned {sh([[1, 2, 3]])!r}, expected (1, 3)."
assert tr([[1, 2, 3], [4, 5, 6]]) == [[1, 4], [2, 5], [3, 6]], f"transpose returned {tr([[1, 2, 3], [4, 5, 6]])!r}."
assert mm([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]], f"matmul([[1, 2], [3, 4]], [[5, 6], [7, 8]]) returned {mm([[1, 2], [3, 4]], [[5, 6], [7, 8]])!r}, expected [[19, 22], [43, 50]]."
assert mm([[1, 2, 3]], [[1], [1], [1]]) == [[6]], "A 1 × 3 times a 3 × 1 matrix should give [[6]]."
assert mm([[2], [3]], [[1, 4]]) == [[2, 8], [3, 12]], "A 2 × 1 times a 1 × 2 matrix should give a 2 × 2 matrix."
try:
    mm([[1, 2]], [[1, 2]])
except ValueError:
    pass
else:
    raise AssertionError("matmul of a 1 × 2 and a 1 × 2 matrix should raise ValueError: the inner sizes don't match.")
