import random as _r
mp, sc = ns.get("make_pairs"), ns.get("score")
assert mp and sc, "Keep make_pairs and score."
ps = mp(["b1", "b2", "b3"], ["t1", "t2", "t3"], 1)
assert len(ps) == 3, "make_pairs should return one pair per answer."
rng = _r.Random(1)
for i, p in enumerate(ps):
    exp = "A" if rng.random() < 0.5 else "B"
    assert p["tuned"] == exp, f"Pair {i}: with seed 1 tuned should be {exp!r} (one rng.random() call per pair)."
    assert p[exp] == f"t{i+1}" and p["B" if exp == "A" else "A"] == f"b{i+1}", f"Pair {i} has the answers in the wrong slots."
pairs = [{"tuned": "A"}, {"tuned": "B"}, {"tuned": "A"}, {"tuned": "B"}]
got = sc(pairs, ["A", "B", "tie", "A"])
assert tuple(got) == (0.625, 0.151, 1.099), f"score should give (0.625, 0.151, 1.099), got {got!r}."
