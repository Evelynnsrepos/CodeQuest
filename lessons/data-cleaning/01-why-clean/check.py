ce, pr = ns.get("count_empty"), ns.get("profile")
assert ce and pr, "Keep count_empty and profile."
rows = [{"a": "x", "b": None}, {"a": "  ", "b": "1"}, {"a": "", "b": "\t"}]
assert ce(rows, "a") == 2, "count_empty: '' and '  ' are both empty."
assert ce(rows, "b") == 2, "count_empty: None and a tab-only value count too."
assert pr(rows) == {"a": 2, "b": 2}, f"profile(rows) should be {{'a': 2, 'b': 2}}, got {pr(rows)!r}."
assert pr([]) == {}, "profile([]) is {}."
