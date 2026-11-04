pf, zs = ns.get("patchify"), ns.get("zero_shot")
assert pf and zs, "Keep patchify and zero_shot."
img = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
got = pf(img, 2)
assert got == [[1, 2, 5, 6], [3, 4, 7, 8], [9, 10, 13, 14], [11, 12, 15, 16]], f"patchify(img, 2) gave {got!r}."
assert pf(img, 4) == [list(range(1, 17))], "One patch covering everything is the whole image flattened."
assert len(pf([[0] * 6 for _ in range(6)], 3)) == 4, "A 6×6 image with p=3 has 4 patches."
assert zs([1.0, 0.0], [[0.0, 1.0], [10.0, 1.0], [1.0, 1.0]], ["a", "b", "c"]) == "b", "Use cosine similarity (direction), not the dot product."
