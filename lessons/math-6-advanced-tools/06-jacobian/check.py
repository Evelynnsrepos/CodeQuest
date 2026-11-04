import math
ja, mm, cj = ns.get("jacobian"), ns.get("matmul"), ns.get("chain_jacobian")
assert ja and mm and cj, "Keep jacobian, matmul and chain_jacobian."
close = lambda A, B, t=1e-4: len(A) == len(B) and all(abs(a - b) < t for ra, rb in zip(A, B) for a, b in zip(ra, rb))
f = lambda v: [v[0] * v[1], v[0] + v[1] ** 2]
assert close(ja(f, [2.0, 3.0]), [[3, 2], [1, 6]]), f"J at (2, 3) = [[3, 2], [1, 6]], got {ja(f, [2.0, 3.0])!r}."
g3 = lambda v: [v[0], v[1], v[0] * v[1]]
assert close(ja(g3, [1.0, 2.0]), [[1, 0], [0, 1], [2, 1]]), "3 outputs, 2 inputs: a 3 × 2 table (rows = outputs)."
assert mm([[1, 2]], [[3], [4]]) == [[11]], "matmul."
g = lambda v: [math.sin(v[0]) + v[1], v[0] * v[1]]
x = [2.0, 3.0]
fx = f(x)
direct = ja(lambda v: g(f(v)), x)
assert close(cj(f, g, x), direct, 1e-3), "chain_jacobian must equal the Jacobian of g(f(x)) computed directly."
