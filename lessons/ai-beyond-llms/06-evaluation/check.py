P, R, F = ns.get("precision"), ns.get("recall"), ns.get("f1")
assert P and R and F, "Keep precision, recall and f1."
t = [1, 1, 1, 0, 0, 0]
p = [1, 1, 0, 1, 0, 0]
assert abs(P(t, p) - 2 / 3) < 1e-12, f"TP=2, FP=1: precision 2/3, got {P(t, p)!r}."
assert abs(R(t, p) - 2 / 3) < 1e-12, f"TP=2, FN=1: recall 2/3, got {R(t, p)!r}."
assert abs(F(t, p) - 2 / 3) < 1e-12, "F1 of 2/3 and 2/3 is 2/3."
t2, p2 = [1, 1, 1, 1], [1, 0, 0, 0]
assert abs(F(t2, p2) - 0.4) < 1e-12, f"precision 1, recall 0.25 -> F1 0.4, got {F(t2, p2)!r}."
assert P([1, 0], [0, 0]) == 0.0 and F([1, 0], [0, 0]) == 0.0, "No positive predictions: precision and F1 are 0.0 (no division by zero)."
assert R([0, 0], [1, 0]) == 0.0, "No actual positives: recall is 0.0."
