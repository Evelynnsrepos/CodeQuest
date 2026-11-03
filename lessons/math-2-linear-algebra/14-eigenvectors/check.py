import math
ie, pi = ns.get("is_eigenvector"), ns.get("power_iteration")
assert ie and pi, "Keep is_eigenvector and power_iteration."
A = [[2, 1], [1, 2]]
assert ie(A, [1, 1]) is True and ie(A, [1, -1]) is True, "(1, 1) and (1, −1) are eigenvectors of [[2,1],[1,2]]."
assert ie(A, [1, 0]) is False, "(1, 0) gets turned: not an eigenvector."
assert ie([[2, 0], [0, 1]], [0, 5]) is True, "(0, 5) is only stretched by 1."
lam, v = pi(A, 60)
assert abs(lam - 3) < 1e-6, f"The biggest eigenvalue of [[2,1],[1,2]] is 3, got {lam!r}."
assert abs(abs(v[0]) - 1 / math.sqrt(2)) < 1e-6 and abs(abs(v[1]) - 1 / math.sqrt(2)) < 1e-6, f"The unit eigenvector is (0.707, 0.707), got {v!r}."
lam2, _ = pi([[3, 1], [0, 1]], 80)
assert abs(lam2 - 3) < 1e-6, "power_iteration([[3,1],[0,1]]) should find λ = 3."
