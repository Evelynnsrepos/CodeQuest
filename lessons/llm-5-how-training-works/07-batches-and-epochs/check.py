mb, spe, tr = ns.get("make_batches"), ns.get("steps_per_epoch"), ns.get("train")
assert mb and spe and tr, "Keep make_batches, steps_per_epoch and train."
assert mb(list(range(7)), 3) == [[0, 1, 2], [3, 4, 5], [6]], f"make_batches(range(7), 3) returned {mb(list(range(7)), 3)!r}, expected [[0, 1, 2], [3, 4, 5], [6]]."
assert spe(100, 32) == 4 and spe(64, 32) == 2, f"steps_per_epoch(100, 32) should be 4 and steps_per_epoch(64, 32) should be 2."
data = [(0.0, 1.0), (1.0, 3.0), (2.0, 5.0), (3.0, 7.0)]
w, b = tr(data, 0.05, 300, 2)
assert abs(w - 2) < 0.01 and abs(b - 1) < 0.01, f"train on y = 2x + 1 with batch size 2 ended at w={w:.3f}, b={b:.3f}."
w1, b1 = tr(data, 0.1, 1, 4)
assert abs(w1 - 1.7) < 1e-9 and abs(b1 - 0.8) < 1e-9, f"One epoch with one full batch and lr 0.1 should give w=1.7, b=0.8, got {w1}, {b1}."
