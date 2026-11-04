import math


def perplexity(probs):
    return math.exp(-sum(math.log(p) for p in probs) / len(probs))


def ppl_from_loss(loss):
    return math.exp(loss)


def loss_from_ppl(ppl):
    return math.log(ppl)


print(perplexity([0.5, 0.25]), ppl_from_loss(2.1), loss_from_ppl(1000))
