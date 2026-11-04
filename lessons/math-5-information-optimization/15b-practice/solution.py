import math


def bits(p):
    return -math.log2(p)


def token_loss(p):
    return -math.log(p)


def perplexity(loss):
    return math.exp(loss)


def kl(p, q):
    return sum(pi * math.log(pi / qi) for pi, qi in zip(p, q) if pi > 0)


def worst_error(bits, m):
    return 2 * m / (2 ** bits - 1) / 2


print(bits(1 / 8), token_loss(0.25), perplexity(math.log(4)), kl([0.5, 0.5], [0.9, 0.1]), worst_error(4, 1))
