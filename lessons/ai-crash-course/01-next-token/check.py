nw, ge = ns.get("next_word"), ns.get("generate")
assert nw and ge, "Keep next_word and generate."
counts = {"once": {"upon": 5}, "upon": {"a": 5}, "a": {"time": 9, "hill": 1}, "time": {"there": 4}}
assert nw(counts, "a") == "time" and nw(counts, "zebra") is None, "next_word: the most frequent follower, or None."
assert ge(counts, "once", 5) == "once upon a time there", f"Got {ge(counts, 'once', 5)!r}."
assert ge(counts, "once", 2) == "once upon a", "Exactly n new words."
