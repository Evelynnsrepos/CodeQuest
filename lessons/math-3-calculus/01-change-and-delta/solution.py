def delta(before, after):
    return after - before


def avg_rate(f, a, b):
    return (f(b) - f(a)) / (b - a)


def deltas(values):
    return [values[i + 1] - values[i] for i in range(len(values) - 1)]


print(delta(2.5, 1.9), avg_rate(lambda s: 3 * s, 1, 4), deltas([2, 5, 4]))
