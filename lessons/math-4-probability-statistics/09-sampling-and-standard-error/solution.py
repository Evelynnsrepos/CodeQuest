import math
import random


def simulate_mean(seed, n):
    rng = random.Random(seed)
    return sum(rng.randint(1, 6) for _ in range(n)) / n


def standard_error(sigma, n):
    return sigma / math.sqrt(n)


def n_needed(sigma, target_se):
    return math.ceil((sigma / target_se) ** 2 - 1e-9)


print(simulate_mean(1, 10), simulate_mean(1, 10000), standard_error(1.71, 100), n_needed(1.71, 0.05))
