import math


def goodness(h):
    total = 0
    for x in h:
        total = total + x * x
    return total


def softplus(x):
    if x > 30:
        return x
    return math.log(1 + math.exp(x))


def ff_loss(h_pos, h_neg, theta):
    return softplus(theta - goodness(h_pos)) + softplus(goodness(h_neg) - theta)


def normalize(h):
    length = math.sqrt(goodness(h))
    if length == 0:
        return h
    out = []
    for x in h:
        out.append(x / length)
    return out


real = [2.0, 1.5, 0.0, 1.0]     # activities on a positive example
fake = [0.3, 0.1, 0.4, 0.2]     # activities on a negative example
print("goodness real:", goodness(real), " fake:", round(goodness(fake), 2))
print("loss with θ = 2:", round(ff_loss(real, fake, 2.0), 4))
print("loss if the layer had it backwards:", round(ff_loss(fake, real, 2.0), 4))
print("normalized:", [round(x, 3) for x in normalize(real)])
