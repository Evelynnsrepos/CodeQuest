em, mo, sp = ns.get("ema"), ns.get("momentum_step"), ns.get("speedup")
assert em and mo and sp, "Keep ema, momentum_step and speedup."
r = em([1, 1, 1], 0.9)
assert len(r) == 3 and all(abs(a - b) < 1e-12 for a, b in zip(r, [0.1, 0.19, 0.271])), f"ema([1, 1, 1], 0.9) = [0.1, 0.19, 0.271], got {r!r}."
r = em([2.3, 2.1, 2.4], 0.5)
assert abs(r[-1] - (0.5 * (0.5 * 1.15 + 1.05) + 1.2)) < 1e-12, "ema with β = 0.5."
th, v = mo([0.0], [1.0], [1.0], 0.1, 0.9)
assert abs(v[0] - 1.9) < 1e-12 and abs(th[0] + 0.19) < 1e-12, f"v = 0.9·1 + 1 = 1.9, θ = 0 − 0.1·1.9 = −0.19, got {(th, v)!r}."
th, v = [5.0, -5.0], [0.0, 0.0]
for _ in range(300):
    th, v = mo(th, v, [2 * th[0], 2 * th[1]], 0.05, 0.9)
assert abs(th[0]) < 1e-3 and abs(th[1]) < 1e-3, "Momentum should still reach the bottom of x² + y²."
assert abs(sp(0.9) - 10) < 1e-9 and abs(sp(0.99) - 100) < 1e-9, "speedup = 1 / (1 − β)."
