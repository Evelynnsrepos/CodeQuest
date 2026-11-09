nw, ge = ns.get("next_word"), ns.get("generate")
assert nw and ge, "Keep next_word and generate."
counts = {"once": {"upon": 5}, "upon": {"a": 5}, "a": {"time": 9, "hill": 1}, "time": {"there": 4}}
assert nw(counts, "zebra") is None, "next_word: a word that isn't in counts gives back None (step 1)."
assert nw(counts, "a") == "time" and nw({"x": {"p": 1, "q": 3, "r": 2}}, "x") == "q", f"next_word: the follower with the biggest count. next_word(counts, 'a') gave {nw(counts, 'a')!r}."
assert ge(counts, "once", 2) == "once upon a", f"generate(counts, 'once', 2) should be 'once upon a' (exactly 2 new words), got {ge(counts, 'once', 2)!r}."
assert ge(counts, "once", 5) == "once upon a time there", f"Stop early when next_word gives None: got {ge(counts, 'once', 5)!r}."
