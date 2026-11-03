it, sp = ns.get("image_tokens"), ns.get("splice")
assert it and sp, "Keep image_tokens and splice."
assert it(336, 336, 14, 1) == 576, f"336×336 with 14-pixel patches is 24·24 = 576 tokens, got {it(336, 336, 14, 1)!r}."
assert it(448, 448, 14, 2) == 256, "448×448, patch 14, merge 2: 32·32 / 4 = 256."
assert it(224, 112, 16, 1) == 98, "Non-square: 14 · 7 = 98."
toks = ["a", "<img>", "b", "<img>"]
orig = list(toks)
got = sp(toks, [[1, 2], [3]], "<img>")
assert got == ["a", 1, 2, "b", 3], f"splice should give ['a', 1, 2, 'b', 3], got {got!r}."
assert toks == orig, "Don't change the input list."
assert sp(["x"], [], "<img>") == ["x"], "No marker: the tokens come back unchanged."
