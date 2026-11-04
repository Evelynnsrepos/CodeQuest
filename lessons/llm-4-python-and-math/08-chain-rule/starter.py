import math


def softmax(z):
    m = max(z)
    e = [math.exp(v - m) for v in z]
    s = sum(e)
    return [v / s for v in e]


def cross_entropy(logits, target):
    return -math.log(softmax(logits)[target])


def sigmoid(z):
    return 0


def dsigmoid(z):
    return 0


def ce_grad(logits, target):
    return []


logits = [2.0, 1.0, 0.1]
print("probabilities:", [round(p, 3) for p in softmax(logits)])
print("loss if the true token is 1:", round(cross_entropy(logits, 1), 3))
print("gradient:", [round(g, 3) for g in ce_grad(logits, 1)])
