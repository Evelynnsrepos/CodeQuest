import math


def likelihood(p, flips):
    return 0


def log_likelihood(p, flips):
    return 0


def best_p(flips):
    return 0.5


def nll_per_token(probs):
    return 0


flips = [1] * 7 + [0] * 3
print(likelihood(0.7, flips), log_likelihood(0.7, flips), best_p(flips), nll_per_token([0.5, 0.25]))
