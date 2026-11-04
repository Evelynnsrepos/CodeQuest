import math


def logsumexp(xs):
    m = max(xs)
    return m + math.log(sum(math.exp(x - m) for x in xs))


def log_softmax(xs):
    lse = logsumexp(xs)
    return [x - lse for x in xs]


def softmax(xs):
    m = max(xs)
    es = [math.exp(x - m) for x in xs]
    s = sum(es)
    return [e / s for e in es]


print(logsumexp([1, 2, 3]), log_softmax([1, 2, 3]), softmax([1000, 1000]))
