import math
sd, ms, ic = ns.get("second_derivative"), ns.get("max_stable_lr"), ns.get("is_convex")
assert sd and ms and ic, "Keep second_derivative, max_stable_lr and is_convex."
L = lambda w: (w - 3) ** 2
assert abs(sd(L, 0) - 2) < 1e-4, f"Curvature of (w − 3)² is 2, got {sd(L, 0)!r}."
assert abs(sd(lambda x: x ** 3, 2) - 12) < 1e-3, "x³ has f'' = 6x → 12 at 2."
assert abs(sd(math.exp, 0) - 1) < 1e-4, "e^x is its own second derivative."
assert ms(2) == 1 and ms(50) == 0.04, "max_stable_lr = 2 / curvature."
assert ic(L, [-5, 0, 5]) is True and ic(math.exp, [-2, 0, 2]) is True, "Bowls are convex."
assert ic(math.sin, [0, 1, 2, 3]) is False, "sin curves downward between 0 and π: not convex."
w = 0
for _ in range(50):
    w -= 0.9 * ms(2) * 2 * (w - 3)
assert abs(w - 3) < 1e-3, "Just below the limit should still converge."
