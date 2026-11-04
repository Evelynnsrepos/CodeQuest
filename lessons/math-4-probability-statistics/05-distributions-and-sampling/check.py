import random
fs, cd, sm = ns.get("from_samples"), ns.get("cdf"), ns.get("sample")
assert fs and cd and sm, "Keep from_samples, cdf and sample."
assert fs([1, 3, 3, 6]) == {1: 0.25, 3: 0.5, 6: 0.25}, f"from_samples([1, 3, 3, 6]) wrong, got {fs([1, 3, 3, 6])!r}."
d = {"cat": 0.5, "dog": 0.3, "fish": 0.2}
assert abs(cd(d, "cat") - 0.5) < 1e-12 and abs(cd(d, "dog") - 0.8) < 1e-12 and abs(cd(d, "fish") - 1) < 1e-12, "cdf is the running total."
assert [sm(d, u) for u in (0.0, 0.12, 0.49, 0.5, 0.65, 0.79, 0.8, 0.93)] == ["cat", "cat", "cat", "dog", "dog", "dog", "fish", "fish"], "sample: first outcome whose running total is > u."
rng = random.Random(0)
counts = fs([sm(d, rng.random()) for _ in range(20000)])
assert all(abs(counts[k] - d[k]) < 0.02 for k in d), f"Sampling 20000 times should match the distribution, got {counts!r}."
