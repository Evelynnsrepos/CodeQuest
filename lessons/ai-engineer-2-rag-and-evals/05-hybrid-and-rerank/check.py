r, rr, ov = ns.get("rrf"), ns.get("rerank"), ns.get("overlap_scorer")
assert r and rr and ov, "Keep rrf, rerank and overlap_scorer."
assert r([["a", "b", "c"], ["c", "a", "d"]]) == ["a", "c", "b", "d"], f"a: 1/61 + 1/62; c: 1/63 + 1/61. Got {r([['a', 'b', 'c'], ['c', 'a', 'd']])!r}."
assert r([["x"], ["y"]]) == ["x", "y"], "Ties: alphabetical."
assert r([["a", "b"]], k=0) == ["a", "b"], "Use the k you are given."
assert abs(ov("Delete old generations", "delete OLD nix stuff") - 2 / 3) < 1e-9, "overlap_scorer: share of distinct query words found (lowercase)."
cands = [{"text": "nix flakes pin inputs"}, {"text": "delete old nix generations"}, {"text": "old git branches"}]
got = rr("delete old generations", cands, ov, top=2)
assert [c["text"] for c in got] == ["delete old nix generations", "old git branches"], f"Got {got!r}."
