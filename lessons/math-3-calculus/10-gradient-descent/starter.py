def grad_mse(w, b, xs, ys):
    n = len(xs)
    errs = [w * x + b - y for x, y in zip(xs, ys)]
    return (sum(2 * e * x for e, x in zip(errs, xs)) / n, sum(2 * e for e in errs) / n)


def step(params, grads, lr):
    return params


def minimize(grad_fn, start, lr, steps):
    return start


def fit_line(xs, ys, lr, steps):
    return (0, 0)


print(step([0], [-6], 0.1), minimize(lambda p: [2 * (p[0] - 3)], [0], 0.1, 100), fit_line([1, 2, 3], [5, 7, 9], 0.05, 2000))
