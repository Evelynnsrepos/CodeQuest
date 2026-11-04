def partial(f, point, i, h=1e-5):
    up, down = list(point), list(point)
    up[i] += h
    down[i] -= h
    return (f(*up) - f(*down)) / (2 * h)


def loss_partials(w, b, x, y):
    err = w * x + b - y
    return (2 * err * x, 2 * err)


L = lambda w, b: (w * 2 + b - 7) ** 2
print(partial(L, [1, 1], 0), partial(L, [1, 1], 1), loss_partials(1, 1, 2, 7))
