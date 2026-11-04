st, mi, fl = ns.get("step"), ns.get("minimize"), ns.get("fit_line")
assert st and mi and fl, "Keep step, minimize and fit_line."
r = st([0], [-6], 0.1)
assert abs(r[0] - 0.6) < 1e-12, f"step([0], [-6], 0.1) should be [0.6] (minus the gradient!), got {r!r}."
r = st([1, 2], [0.5, -1], 0.2)
assert abs(r[0] - 0.9) < 1e-12 and abs(r[1] - 2.2) < 1e-12, "Update every parameter."
r = mi(lambda p: [2 * (p[0] - 3)], [0], 0.1, 100)
assert abs(r[0] - 3) < 1e-6, f"Minimising (w − 3)² should reach 3, got {r!r}."
r = mi(lambda p: [2 * (p[0] - 1), 4 * (p[1] + 2)], [5, 5], 0.1, 200)
assert abs(r[0] - 1) < 1e-6 and abs(r[1] + 2) < 1e-6, "Two parameters: (x − 1)² + 2(y + 2)² → (1, −2)."
w, b = fl([1, 2, 3], [5, 7, 9], 0.05, 2000)
assert abs(w - 2) < 1e-3 and abs(b - 3) < 1e-3, f"Points on y = 2x + 3 should give (2, 3), got {(w, b)!r}."
