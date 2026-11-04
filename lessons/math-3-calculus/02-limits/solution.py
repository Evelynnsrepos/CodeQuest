def table(f, a, hs):
    return [f(a + h) for h in hs]


def estimate_limit(f, a):
    return (f(a + 1e-6) + f(a - 1e-6)) / 2


def has_limit(f, a):
    return abs(f(a + 1e-6) - f(a - 1e-6)) < 1e-3


g = lambda x: (x * x - 1) / (x - 1)
print(table(g, 1, [0.1, 0.01, -0.01]), estimate_limit(g, 1), has_limit(lambda x: abs(x) / x, 0))
