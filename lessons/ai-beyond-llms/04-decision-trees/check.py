g, bs = ns.get("gini"), ns.get("best_split")
assert g and bs, "Keep gini and best_split."
assert g(["a", "a", "a"]) == 0, "A pure group has gini 0."
assert abs(g(["a", "b"]) - 0.5) < 1e-12, "50/50 has gini 0.5."
assert abs(g(["a", "b", "c"]) - (1 - 3 / 9)) < 1e-12, "Three equal classes: 1 - 3·(1/3)² = 0.667."
got = bs([1, 2, 3, 4], ["n", "n", "y", "y"])
assert got == (2, 0.0), f"Splitting at x <= 2 separates perfectly: expected (2, 0.0), got {got!r}."
got = bs([5, 1, 3, 2], ["y", "n", "y", "n"])
assert got == (2, 0.0), f"Unsorted input: the best split is still x <= 2, got {got!r}."
got = bs([1, 2, 3], ["a", "b", "a"])
assert got == (1, 0.3333), f"Expected (1, 0.3333) (ties keep the first threshold), got {got!r}."
