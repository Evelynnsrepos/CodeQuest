import math


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def grad_check(f, df, x):
    num = (f(x + 1e-5) - f(x - 1e-5)) / 2e-5
    return abs(df(x) - num) / max(1, abs(num))


def avg_loss(w, b, xs, ys):
    return sum((sigmoid(w * x + b) - y) ** 2 for x, y in zip(xs, ys)) / len(xs)


def train(xs, ys, lr, steps):
    w = b = 0.0
    n = len(xs)
    for _ in range(steps):
        gw = gb = 0.0
        for x, y in zip(xs, ys):
            a = sigmoid(w * x + b)
            shared = 2 * (a - y) * a * (1 - a)
            gw += shared * x / n
            gb += shared / n
        w, b = w - lr * gw, b - lr * gb
    return (w, b)


xs, ys = [-2, -1, 1, 2], [0, 0, 1, 1]
w, b = train(xs, ys, 1.0, 500)
print("check", grad_check(lambda x: x ** 3, lambda x: 3 * x * x, 2), "loss", avg_loss(0, 0, xs, ys), "->", avg_loss(w, b, xs, ys))
