cm, mm, mf = ns.get("can_multiply"), ns.get("matmul"), ns.get("matmul_flops")
assert cm and mm and mf, "Keep can_multiply, matmul and matmul_flops."
assert cm((32, 4096), (4096, 1024)) is True and cm((2, 3), (2, 3)) is False, "Inner sizes must match: (2×3)(2×3) can't be multiplied."
assert mm([[1, 2], [3, 4]], [[5, 6], [7, 8]]) == [[19, 22], [43, 50]], f"Got {mm([[1, 2], [3, 4]], [[5, 6], [7, 8]])!r}."
got = mm([[1, 2, 3]], [[1], [0], [2]])
assert got == [[7]], f"(1×3)(3×1) is 1×1: [[7]], got {got!r}."
got = mm([[1], [2]], [[3, 4]])
assert got == [[3, 4], [6, 8]], f"(2×1)(1×2) is 2×2: [[3, 4], [6, 8]], got {got!r}."
try:
    mm([[1, 2]], [[1, 2]])
except ValueError:
    pass
else:
    raise AssertionError("matmul should raise ValueError for (1×2)(1×2).")
assert mf(2, 3, 4) == 48, "2·2·3·4 = 48."
