import math


def likelihood(p, flips):
    return math.prod(p if f else 1 - p for f in flips)


def log_likelihood(p, flips):
    return sum(math.log(p if f else 1 - p) for f in flips)


def best_p(flips):
    grid = [i / 100 for i in range(1, 100)]
    return max(grid, key=lambda p: log_likelihood(p, flips))


def nll_per_token(probs):
    return -sum(math.log(p) for p in probs) / len(probs)


flips = [1] * 7 + [0] * 3
print(likelihood(0.7, flips), log_likelihood(0.7, flips), best_p(flips), nll_per_token([0.5, 0.25]))
