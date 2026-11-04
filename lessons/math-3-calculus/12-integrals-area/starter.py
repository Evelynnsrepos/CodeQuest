def riemann(f, a, b, n):
    return 0


def prob_between(density, a, b):
    return 0


def auc(points):
    return 0


print(riemann(lambda x: 2 * x, 0, 3, 3), riemann(lambda x: x * x, 0, 1, 1000), auc([(0, 0), (0.5, 0.8), (1, 1)]))
