f = ns.get
for name in ("fits", "full_ft_gb", "best_step", "win_interval", "clear_win"):
    assert f(name), f"Keep the function {name}."
assert f("fits")(8, 16, 12) is False, "8B at 16 bits is 16 GB of weights + 1.5: does it fit in 12?"
assert f("fits")(8, 4.5, 12) is True, "8B at 4.5 bits is 4.5 GB + 1.5 GB: that fits in 12."
assert f("fits")(14, 4.5, 8) is False and f("fits")(14, 4.5, 9.5) is True, "fits: 14B at 4.5 bits = 7.875 GB + 1.5 overhead (use <=)."
assert abs(f("full_ft_gb")(8) - 128) < 1e-9 and abs(f("full_ft_gb")(0.5) - 8) < 1e-9, "full_ft_gb: 16 bytes per parameter."
assert f("best_step")([(200, 1.9), (400, 1.6), (600, 1.5), (800, 1.7)]) == 600, "best_step: the step with the LOWEST eval_loss."
assert f("best_step")([(100, 2.0), (200, 2.2)]) == 100, "best_step: the first one can be the best."
lo, hi = f("win_interval")(60, 100)
assert abs(lo - 0.50398) < 1e-4 and abs(hi - 0.69602) < 1e-4, f"win_interval(60, 100) ≈ (0.504, 0.696), got {(lo, hi)!r}."
assert f("clear_win")(60, 100) is True and f("clear_win")(55, 100) is False and f("clear_win")(6, 10) is False, "clear_win: only when the whole interval is above 0.5."

A = ns.get("ANSWERS")
assert isinstance(A, dict), "Keep the ANSWERS dict."
key = {1: 'b', 2: 'c', 3: 'd', 4: 'a', 5: 'c', 6: 'b'}
hint = {1: 'what has already influenced your choices?', 2: 'what should the model learn to write?', 3: 'what is the model doing once eval_loss rises?', 4: 'who might be biased, and toward what?', 5: 'which method updates facts cheaply, and what does pasting everything cost every time?', 6: 'what can training on one kind of output do to the others?'}
for q in key:
    got = str(A.get(q, "")).strip().lower()
    assert got, f"Question {q} has no answer yet."
    assert got in "abcd" and len(got) == 1, f"Question {q}: answer with one letter, a to d."
    assert got == key[q], f"Question {q} isn't right. Hint: {hint[q]}."
