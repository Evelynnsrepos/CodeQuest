import math
pr, tl, ac = ns.get("predict"), ns.get("train_logistic"), ns.get("accuracy")
assert pr and tl and ac, "Keep predict, train_logistic and accuracy."
assert abs(pr([2.0, -1.0], 0.5, [1.0, 3.0]) - 1 / (1 + math.exp(0.5))) < 1e-12, "predict should be sigmoid(w·x + b)."
w, b = tl([[1.0], [2.0]], [0, 1], 1.0, 1)
# step 1: p=0.5, err=0.5 -> w=-0.5, b=-0.5; step 2: p=sigmoid(-1.5)
p2 = 1 / (1 + math.exp(1.5)); err = p2 - 1
assert abs(w[0] - (-0.5 - 2 * err)) < 1e-9 and abs(b - (-0.5 - err)) < 1e-9, f"After one epoch on two examples (in order) got w={w!r}, b={b!r}. Update after every example."
X = [[0.0, 1.0], [1.0, 0.0], [0.2, 0.9], [0.9, 0.1]]
y = [0, 1, 0, 1]
w, b = tl(X, y, 0.5, 200)
assert ac(w, b, X, y) == 1.0, "This data is easy to separate; after training accuracy should be 1.0."
assert ac([0.0, 0.0], 0.0, X, y) == 0.5, "With p = 0.5 everywhere, everything is predicted 1, so accuracy is 0.5."
