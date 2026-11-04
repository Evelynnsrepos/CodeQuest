import math


def conditional(p_ab, p_b):
    return p_ab / p_b


def from_counts(both, b_count):
    return both / b_count


def sequence_prob(cond_probs):
    return math.prod(cond_probs)


print(conditional(0.24, 0.3), from_counts(24, 30), sequence_prob([0.05, 0.02, 0.3]))
