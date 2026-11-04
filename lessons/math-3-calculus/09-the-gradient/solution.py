def gradient(f, point, h=1e-5):
    out = []
    for i in range(len(point)):
        up, down = list(point), list(point)
        up[i] += h
        down[i] -= h
        out.append((f(*up) - f(*down)) / (2 * h))
    return out


def grad_mse(w, b, xs, ys):
    n = len(xs)
    errs = [w * x + b - y for x, y in zip(xs, ys)]
    return (sum(2 * e * x for e, x in zip(errs, xs)) / n, sum(2 * e for e in errs) / n)


print(gradient(lambda x, y: x * x + 3 * y, [1, 2]), grad_mse(1, 1, [2], [7]))
