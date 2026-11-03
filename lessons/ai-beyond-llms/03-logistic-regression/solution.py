import math


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def predict(w, b, x):
    return sigmoid(sum(wi * xi for wi, xi in zip(w, x)) + b)


def train_logistic(X, y, lr, epochs):
    w, b = [0.0] * len(X[0]), 0.0
    for _ in range(epochs):
        for x, t in zip(X, y):
            err = predict(w, b, x) - t
            w = [wi - lr * err * xi for wi, xi in zip(w, x)]
            b -= lr * err
    return w, b


def accuracy(w, b, X, y):
    return sum((predict(w, b, x) >= 0.5) == bool(t) for x, t in zip(X, y)) / len(X)


hours = [[0.5], [1.0], [1.5], [2.0], [3.0], [3.5], [4.0], [5.0]]
passed = [0, 0, 0, 1, 0, 1, 1, 1]
w, b = train_logistic(hours, passed, lr=0.5, epochs=300)
print("w, b:", [round(v, 2) for v in w], round(b, 2))
for h in [1.0, 2.5, 4.5]:
    print(f"{h} h of study -> P(pass) = {predict(w, b, [h]):.2f}")
print("accuracy:", accuracy(w, b, hours, passed))
