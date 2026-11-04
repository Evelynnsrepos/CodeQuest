sh, en, co = ns.get("shape"), ns.get("entry"), ns.get("column")
assert sh and en and co, "Keep shape, entry and column."
A = [[1, 2, 3], [4, 5, 6]]
assert sh(A) == (2, 3), f"shape should be (2, 3), got {sh(A)!r}."
assert sh([[1], [2], [3], [4]]) == (4, 1), "A column vector is 4 × 1."
assert en(A, 1, 2) == 2 and en(A, 2, 3) == 6 and en(A, 1, 1) == 1, f"entry(A, 1, 2) should be 2 (row 1, column 2, counting from 1), got {en(A, 1, 2)!r}."
assert co(A, 3) == [3, 6] and co(A, 1) == [1, 4], f"column(A, 3) should be [3, 6], got {co(A, 3)!r}."
