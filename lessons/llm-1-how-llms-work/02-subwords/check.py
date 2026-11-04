f = ns.get("tokens_per_word")
assert f, "Keep the function tokens_per_word."
got = f("The cat sat on the mat.")
assert abs(got - 7 / 6) < 1e-9, f"tokens_per_word('The cat sat on the mat.') returned {got!r}. It has 7 tokens and 6 words, so expected {7/6:.3f}."
got = f("The cat")
assert abs(got - 1.0) < 1e-9, f"tokens_per_word('The cat') returned {got!r}, expected 1.0 (2 tokens, 2 words)."
assert ns.get("german_costs_more") is True, "Look at your output again: which sentence needs more tokens per word? Set german_costs_more to True or False (no quotes)."
