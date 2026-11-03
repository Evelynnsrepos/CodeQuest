ng, gd = ns.get("numeric_gradient"), ns.get("gradient_descent")
assert ng and gd, "Keep numeric_gradient and gradient_descent."
f = lambda p: p[0] ** 2 + 5 * p[0] * p[1] + p[2]
g = ng(f, [1.0, 2.0, 3.0])
assert len(g) == 3 and all(abs(a - b) < 1e-4 for a, b in zip(g, [12, 5, 1])), f"numeric_gradient of x² + 5xy + z at (1, 2, 3) returned {g!r}, expected about [12, 5, 1]."
pt = [1.0, 2.0, 3.0]
ng(f, pt)
assert pt == [1.0, 2.0, 3.0], "numeric_gradient changed the point it was given. Nudge a copy."
end = gd(lambda p: (p[0] - 4) ** 2, [0.0], 0.1, 100)
assert abs(end[0] - 4) < 1e-3, f"gradient_descent on (x − 4)² from 0 ended at {end!r}, expected about [4]."
one = gd(lambda p: p[0] ** 2, [10.0], 0.25, 1)
assert abs(one[0] - 5) < 1e-4, f"One step with lr 0.25 on x² from 10 should land at 10 − 0.25 × 20 = 5, got {one!r}."
