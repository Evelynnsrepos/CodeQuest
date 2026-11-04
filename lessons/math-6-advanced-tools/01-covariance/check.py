import statistics
cv, cm = ns.get("covariance"), ns.get("cov_matrix")
assert cv and cm, "Keep covariance and cov_matrix."
h, s = [1, 2, 3, 4, 5], [50, 55, 65, 70, 80]
assert abs(cv(h, s) - 18.75) < 1e-9, f"covariance(hours, score) = 75 / 4 = 18.75, got {cv(h, s)!r}."
assert abs(cv([1, 2, 3], [3, 2, 1]) + 1) < 1e-9, "Opposite directions → negative (−1 here)."
M = cm([h, s, [2, 2, 2, 2, 2]])
assert abs(M[0][0] - statistics.variance(h)) < 1e-9 and abs(M[1][1] - statistics.variance(s)) < 1e-9, "The diagonal holds each column's variance."
assert abs(M[0][1] - 18.75) < 1e-9 and abs(M[1][0] - 18.75) < 1e-9, "The matrix is symmetric."
assert all(abs(v) < 1e-12 for v in M[2]), "A constant column has 0 covariance with everything."
