import math
sq, sl, ch = ns.get("d_square_of_linear"), ns.get("d_sigmoid_of_linear"), ns.get("chain")
assert sq and sl and ch, "Keep d_square_of_linear, d_sigmoid_of_linear and chain."
num = lambda f, x: (f(x + 1e-5) - f(x - 1e-5)) / 2e-5
assert abs(sq(3, 1, 2) - 42) < 1e-9, f"(3x + 1)² at 2 has slope 42, got {sq(3, 1, 2)!r}."
assert abs(sq(-2, 5, 1.5) - num(lambda x: (-2 * x + 5) ** 2, 1.5)) < 1e-5, "Check d_square_of_linear against the numeric slope."
sg = lambda z: 1 / (1 + math.exp(-z))
assert abs(sl(2, 0, 0) - 0.5) < 1e-12, f"σ(2x) at 0: 0.25 · 2 = 0.5, got {sl(2, 0, 0)!r}."
assert abs(sl(-1.5, 0.3, 0.8) - num(lambda x: sg(-1.5 * x + 0.3), 0.8)) < 1e-6, "Check d_sigmoid_of_linear against the numeric slope."
assert ch([14, 3]) == 42 and ch([0.5, 0.5, 0.5]) == 0.125 and ch([]) == 1, "chain multiplies all slopes; empty → 1."
