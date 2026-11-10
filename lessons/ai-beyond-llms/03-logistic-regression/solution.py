import math


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def predict(w, b, x):
    z = 0
    for j in range(len(w)):
        z = z + w[j] * x[j]
    return sigmoid(z + b)


def train_logistic(X, y, lr, epochs):
    w = [0.0] * len(X[0])
    b = 0.0
    for epoch in range(epochs):
        for i in range(len(X)):
            x = X[i]
            err = predict(w, b, x) - y[i]
            for j in range(len(w)):
                w[j] = w[j] - lr * err * x[j]
            b = b - lr * err
    return w, b


def accuracy(w, b, X, y):
    correct = 0
    for i in range(len(X)):
        if predict(w, b, X[i]) >= 0.5:
            guess = 1
        else:
            guess = 0
        if guess == y[i]:
            correct = correct + 1
    return correct / len(X)


hours = [[0.5], [1.0], [1.5], [2.0], [3.0], [3.5], [4.0], [5.0]]
passed = [0, 0, 0, 1, 0, 1, 1, 1]
w, b = train_logistic(hours, passed, lr=0.5, epochs=300)
print("w, b:", [round(v, 2) for v in w], round(b, 2))
for h in [1.0, 2.5, 4.5]:
    print(f"{h} h of study -> P(pass) = {predict(w, b, [h]):.2f}")
print("accuracy:", accuracy(w, b, hours, passed))
