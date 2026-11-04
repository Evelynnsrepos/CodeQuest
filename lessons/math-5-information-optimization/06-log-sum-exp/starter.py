import math


def logsumexp(xs):
    return math.log(sum(math.exp(x) for x in xs))


def log_softmax(xs):
    return xs


def softmax(xs):
    return xs


print(logsumexp([1, 2, 3]), log_softmax([1, 2, 3]), softmax([1000, 1000]))
