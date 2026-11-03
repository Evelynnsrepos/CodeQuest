f = ns.get("count_pairs")
assert f, "Keep the function count_pairs."
got = f(["a", "b", "a", "b", "c"])
want = {("a", "b"): 2, ("b", "a"): 1, ("b", "c"): 1}
assert got == want, f"count_pairs(['a', 'b', 'a', 'b', 'c']) returned {got!r}, expected {want!r}."
assert f(["x"]) == {}, "A single token has no neighbours, so count_pairs(['x']) should return {}."
got = f(["l", "o", "w"])
assert got == {("l", "o"): 1, ("o", "w"): 1}, f"count_pairs(['l', 'o', 'w']) returned {got!r}. Use tuples (left, right) as keys."
assert "' low'" in output or "\" low\"" in output, "With a working count_pairs, ' low' should become one token in the printed list."
