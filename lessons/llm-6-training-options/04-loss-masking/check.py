bl, tf = ns.get("build_labels"), ns.get("trained_fraction")
assert bl and tf, "Keep build_labels and trained_fraction."
ids, labels = bl([("user", [5, 6]), ("assistant", [7, 8, 9]), ("user", [10]), ("assistant", [11])])
assert ids == [5, 6, 7, 8, 9, 10, 11], f"input_ids should be all tokens in order, got {ids!r}."
assert labels == [-100, -100, 7, 8, 9, -100, 11], f"labels should keep assistant tokens and mask the rest with -100, got {labels!r}."
assert abs(tf(labels) - 4 / 7) < 1e-9, f"trained_fraction returned {tf(labels)!r}, expected 4/7."
