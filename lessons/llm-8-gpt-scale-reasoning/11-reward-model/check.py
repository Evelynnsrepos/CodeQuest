import math
pl, tr, rw = ns.get("pair_loss"), ns.get("train_reward"), ns["reward"]
assert pl and tr, "Keep pair_loss and train_reward."
assert abs(pl(0.0, 0.0) - math.log(2)) < 1e-12, f"Equal rewards give loss ln 2, got {pl(0.0, 0.0)!r}."
assert abs(pl(2.0, 0.0) - math.log(1 + math.exp(-2))) < 1e-12, "pair_loss(2, 0) should be -ln σ(2)."
assert abs(pl(0.0, 2.0) - math.log(1 + math.exp(2))) < 1e-12, "pair_loss(0, 2) should be -ln σ(-2)."
big = pl(0.0, 1000.0)
assert abs(big - 1000.0) < 1e-6, f"pair_loss(0, 1000) should be about 1000 without overflowing, got {big!r}."
w = tr([([1.0, 0.0], [0.0, 1.0])], 1.0, 1)
assert all(abs(a - b) < 1e-12 for a, b in zip(w, [0.5, -0.5])), f"One step from w = 0 with lr 1 should give [0.5, -0.5], got {w!r}."
pairs = [([1, 0], [0, 0]), ([1, 1], [0, 1]), ([1, 0], [0, 1])]
w = tr(pairs, 0.5, 100)
assert all(rw(w, c) > rw(w, r) for c, r in pairs), "After training, every chosen answer should score higher than its rejected one."
