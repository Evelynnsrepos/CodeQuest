sh, jc, dd = ns.get("shingles"), ns.get("jaccard"), ns.get("dedupe")
assert sh and jc and dd, "Keep shingles, jaccard and dedupe."
got = sh("A b, C d!", 2)
assert got == {("a", "b"), ("b", "c"), ("c", "d")}, f"shingles('A b, C d!', 2) should be {{('a','b'), ('b','c'), ('c','d')}}, got {got!r}."
assert sh("one two", 3) == set(), "A text shorter than n has no shingles."
assert jc({1, 2, 3}, {2, 3, 4}) == 0.5, "jaccard({1,2,3}, {2,3,4}) should be 2/4 = 0.5."
assert jc(set(), set()) == 0.0, "Two empty sets: return 0.0."
docs = ["a b c d e f", "A b c d e f.", "a b c d e x", "p q r s t u", "a b c d e f g"]
got = dd(docs, 0.5)
assert got == ["a b c d e f", "p q r s t u"], f"dedupe(docs, 0.5) should keep the first doc and the unrelated one, got {got!r}."
assert dd(docs, 0.99) == ["a b c d e f", "a b c d e x", "p q r s t u", "a b c d e f g"], "With threshold 0.99 only exact duplicates (after cleaning) should go."
