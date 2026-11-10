import math


def softmax(z):
    m = max(z)
    e = []
    for v in z:
        e.append(math.exp(v - m))
    s = 0
    for v in e:
        s = s + v
    out = []
    for v in e:
        out.append(v / s)
    return out


def cross_entropy(logits, target):
    return -math.log(softmax(logits)[target])


def sigmoid(z):
    return 1 / (1 + math.exp(-z))


def dsigmoid(z):
    s = sigmoid(z)
    return s * (1 - s)


def ce_grad(logits, target):
    grad = softmax(logits)
    grad[target] = grad[target] - 1
    return grad


logits = [2.0, 1.0, 0.1]
print("probabilities:", [round(p, 3) for p in softmax(logits)])
print("loss if the true token is 1:", round(cross_entropy(logits, 1), 3))
print("gradient:", [round(g, 3) for g in ce_grad(logits, 1)])
