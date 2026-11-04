def train(xs, ys, steps, lr):
    w = 0.0
    for _ in range(steps):
        grad = sum(2 * (w * x - y) * x for x, y in zip(xs, ys)) / len(xs)
        w -= lr * grad
    return w


print(train([1, 2, 3], [2, 4, 6], 50, 0.05))
