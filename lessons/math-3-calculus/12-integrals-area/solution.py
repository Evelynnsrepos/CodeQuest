def riemann(f, a, b, n):
    width = (b - a) / n
    return sum(f(a + (i + 0.5) * width) for i in range(n)) * width


def prob_between(density, a, b):
    return riemann(density, a, b, 1000)


def auc(points):
    return sum((x2 - x1) * (y1 + y2) / 2 for (x1, y1), (x2, y2) in zip(points, points[1:]))


print(riemann(lambda x: 2 * x, 0, 3, 3), riemann(lambda x: x * x, 0, 1, 1000), auc([(0, 0), (0.5, 0.8), (1, 1)]))
