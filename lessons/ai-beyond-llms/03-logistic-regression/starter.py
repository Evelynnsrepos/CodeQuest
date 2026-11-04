import math


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def predict(w, b, x):
    return 0.5


def train_logistic(X, y, lr, epochs):
    return [0.0] * len(X[0]), 0.0


def accuracy(w, b, X, y):
    return 0.0


hours = [[0.5], [1.0], [1.5], [2.0], [3.0], [3.5], [4.0], [5.0]]
passed = [0, 0, 0, 1, 0, 1, 1, 1]
w, b = train_logistic(hours, passed, lr=0.5, epochs=300)
print("w, b:", [round(v, 2) for v in w], round(b, 2))
for h in [1.0, 2.5, 4.5]:
    print(f"{h} h of study -> P(pass) = {predict(w, b, [h]):.2f}")
print("accuracy:", accuracy(w, b, hours, passed))
