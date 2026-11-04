import math
gc, al, tr = ns.get("grad_check"), ns.get("avg_loss"), ns.get("train")
assert gc and al and tr, "Keep grad_check, avg_loss and train."
assert gc(lambda x: x ** 3, lambda x: 3 * x * x, 2) < 1e-7, "A correct derivative should pass the check."
assert gc(lambda x: x ** 3, lambda x: 3 * x, 2) > 0.1, "A wrong derivative (3x instead of 3x²) should fail it."
assert abs(gc(lambda x: 1e6 * x * x, lambda x: 2e6 * x + 0.01, 5) - 0.01 / 1e7) < 1e-9, "Divide by max(1, |numeric|)."
assert abs(al(0, 0, [-2, 2], [0, 1]) - 0.25) < 1e-12, "At w = b = 0 every prediction is 0.5: loss 0.25."
xs, ys = [-2, -1, 1, 2], [0, 0, 1, 1]
w, b = tr(xs, ys, 1.0, 500)
assert al(w, b, xs, ys) < 0.05, f"After training the loss should be small, got {al(w, b, xs, ys)!r}."
sg = lambda z: 1 / (1 + math.exp(-z))
assert all((sg(w * x + b) > 0.5) == (y == 1) for x, y in zip(xs, ys)), "Every point should be classified correctly."
w2, b2 = tr([0, 1], [1, 1], 0.5, 1)
assert abs(w2 - 0.0625) < 1e-12 and abs(b2 - 0.125) < 1e-12, f"One step from (0, 0) on points (0,1),(1,1) with lr 0.5 should give (0.0625, 0.125): average the gradients. Got {(w2, b2)!r}."
