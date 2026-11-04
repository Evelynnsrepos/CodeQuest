f = ns.get
for name in ("scores", "weights", "q_new"):
    assert f(name), f"Keep the function {name}."
a, p, r = f("scores")(2, 3, 98, 19897)
assert abs(a - 0.99495) < 1e-4, f"accuracy = (tp + tn) / everything ≈ 0.995, got {a!r}."
assert abs(p - 0.4) < 1e-9, f"precision = tp / (tp + fp) = 0.4, got {p!r}."
assert abs(r - 0.02) < 1e-9, f"recall = tp / (tp + fn) = 0.02: it misses 98% of fraud. Got {r!r}."
assert tuple(f("weights")(28, 28, 3)) == (614656, 9), "weights(28, 28, 3): dense = 784² = 614656, conv = 9."
assert abs(f("q_new")(0, 1, 0, 0.5, 0.9) - 0.5) < 1e-9, "q_new(0, 1, 0, 0.5, 0.9) = 0 + 0.5 · (1 + 0 − 0) = 0.5."
assert abs(f("q_new")(0.2, 0, 1.0, 0.5, 0.9) - 0.55) < 1e-9, "q_new(0.2, 0, 1.0, 0.5, 0.9) = 0.2 + 0.5 · (0 + 0.9 − 0.2) = 0.55."

A = ns.get("ANSWERS")
assert isinstance(A, dict), "Keep the ANSWERS dict."
key = {1: 'b', 2: 'c', 3: 'a', 4: 'd', 5: 'b', 6: 'a'}
hint = {1: 'what wins on spreadsheets?', 2: 'parallelism and long-range links', 3: 'the training loss is MSE on what?', 4: 'zero-shot with captions', 5: 'encoder + projector', 6: 'look at the target in the update'}
for q in key:
    got = str(A.get(q, "")).strip().lower()
    assert got, f"Question {q} has no answer yet."
    assert got in "abcd" and len(got) == 1, f"Question {q}: answer with one letter, a to d."
    assert got == key[q], f"Question {q} isn't right. Hint: {hint[q]}."
