def table(f, a, hs):
    return []


def estimate_limit(f, a):
    return 0


def has_limit(f, a):
    return True


g = lambda x: (x * x - 1) / (x - 1)
print(table(g, 1, [0.1, 0.01, -0.01]), estimate_limit(g, 1), has_limit(lambda x: abs(x) / x, 0))
