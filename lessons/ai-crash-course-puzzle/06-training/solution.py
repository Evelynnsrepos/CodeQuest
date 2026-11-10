def gradient(w, xs, ys):
    total = 0
    for i in range(len(xs)):
        error = w * xs[i] - ys[i]
        total = total + 2 * error * xs[i]
    return total / len(xs)


def train(xs, ys, steps, lr):
    w = 0.0
    for step in range(steps):
        w = w - lr * gradient(w, xs, ys)
    return w


print(gradient(0, [1, 2, 3], [2, 4, 6]), train([1, 2, 3], [2, 4, 6], 50, 0.05))
