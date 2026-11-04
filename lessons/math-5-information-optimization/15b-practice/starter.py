import math


def bits(p):
    return 0


def token_loss(p):
    return 0


def perplexity(loss):
    return 0


def kl(p, q):
    return 0


def worst_error(bits, m):
    return 0


print(bits(1 / 8), token_loss(0.25), perplexity(math.log(4)), kl([0.5, 0.5], [0.9, 0.1]), worst_error(4, 1))
