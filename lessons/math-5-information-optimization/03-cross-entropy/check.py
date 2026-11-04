import math
ce, cl, bl = ns.get("cross_entropy"), ns.get("ce_loss"), ns.get("batch_loss")
assert ce and cl and bl, "Keep cross_entropy, ce_loss and batch_loss."
assert abs(ce([1, 0, 0], [0.7, 0.2, 0.1]) + math.log(0.7)) < 1e-12, f"One-hot cat: 0.357, got {ce([1, 0, 0], [0.7, 0.2, 0.1])!r}."
assert abs(ce([0.9, 0.05, 0.05], [0.7, 0.2, 0.1]) - 0.5160) < 1e-3, "Soft truth: ≈ 0.516."
assert abs(ce([0, 1], [0.0, 1.0])) < 1e-12, "Skip p = 0 terms (no log(0) crash)."
assert abs(ce([0.5, 0.5], [0.5, 0.5]) - math.log(2)) < 1e-12, "When q = p, cross-entropy = entropy."
assert abs(cl([0.7, 0.2, 0.1], 0) + math.log(0.7)) < 1e-12 and abs(cl([0.7, 0.2, 0.1], 2) - math.log(10)) < 1e-12, "ce_loss = −ln q[target]."
assert abs(bl([[0.7, 0.3], [0.1, 0.9]], [0, 1]) - (-(math.log(0.7) + math.log(0.9)) / 2)) < 1e-12, "batch_loss averages."
