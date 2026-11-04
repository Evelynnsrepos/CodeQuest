def gradient(f, point):
    return []


def grad_mse(w, b, xs, ys):
    return (0, 0)


print(gradient(lambda x, y: x * x + 3 * y, [1, 2]), grad_mse(1, 1, [2], [7]))
