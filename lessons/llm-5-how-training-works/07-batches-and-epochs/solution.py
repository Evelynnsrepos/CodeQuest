import math
import random

random.seed(0)
DATA = [(x / 10, 3 * x / 10 + 1 + random.gauss(0, 0.1)) for x in range(40)]
random.shuffle(DATA)


def loss(w, b, data):
    return sum((w * x + b - y) ** 2 for x, y in data) / len(data)


def gradients(w, b, data):
    dw = db = 0.0
    for x, y in data:
        e = w * x + b - y
        dw += 2 * e * x
        db += 2 * e
    return dw / len(data), db / len(data)


def make_batches(data, batch_size):
    return [data[i:i + batch_size] for i in range(0, len(data), batch_size)]


def steps_per_epoch(n_examples, batch_size):
    return math.ceil(n_examples / batch_size)


def train(data, lr, epochs, batch_size):
    w, b = 0.0, 0.0
    for epoch in range(epochs):
        for batch in make_batches(data, batch_size):
            dw, db = gradients(w, b, batch)
            w -= lr * dw
            b -= lr * db
    return w, b


print(len(make_batches(DATA, 16)), "batches,", steps_per_epoch(len(DATA), 16), "steps per epoch")
for lr in [0.001, 0.05, 0.3]:
    w, b = train(DATA, lr, 20, 8)
    print(f"lr={lr}: w={w:.3g}, b={b:.3g}, loss={loss(w, b, DATA):.3g}")
