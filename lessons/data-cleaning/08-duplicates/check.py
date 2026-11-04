d, s, nd = ns.get("dedupe"), ns.get("similarity"), ns.get("near_duplicates")
assert d and s and nd, "Keep dedupe, similarity and near_duplicates."
rows = [{"email": "ada@x.de", "n": 1}, {"email": " ADA@x.de", "n": 2}, {"email": "lin@x.de", "n": 3}]
assert d(rows, ["email"]) == [rows[0], rows[2]], "dedupe: keep the first row per tidied, casefolded key."
rows = [{"a": "x", "b": "1"}, {"a": "x", "b": "2"}, {"a": "X", "b": "1"}]
assert d(rows, ["a", "b"]) == rows[:2], "dedupe: the key combines all listed columns."
assert abs(s("What is a flake?", "what is a flake") - 0.9677) < 1e-3, f"similarity ≈ 0.968, got {s('What is a flake?', 'what is a flake')!r}."
assert s("abc", "ABC ") == 1.0, "similarity compares the key() forms."
qs = ["What is a flake?", "what is a flake", "How do I install Nix?", "What's a flake?"]
assert nd(qs) == [(0, 1), (0, 3)], f"Got {nd(qs)!r}."
assert nd(qs, 0.97) == [], "A higher threshold finds fewer."
