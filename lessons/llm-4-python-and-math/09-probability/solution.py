import random


def expected_value(values, probs):
    total = 0
    for i in range(len(values)):
        total = total + probs[i] * values[i]
    return total


def variance(values, probs):
    mean = expected_value(values, probs)
    total = 0
    for i in range(len(values)):
        total = total + probs[i] * (values[i] - mean) ** 2
    return total


def sample(probs, r):
    running = 0
    for i in range(len(probs)):
        running = running + probs[i]
        if r < running:
            return i
    return len(probs) - 1


die = [1, 2, 3, 4, 5, 6]
fair = [1 / 6] * 6
print("die: E =", round(expected_value(die, fair), 3), " Var =", round(variance(die, fair), 3))

random.seed(42)
probs = [0.5, 0.3, 0.2]
counts = [0, 0, 0]
for _ in range(10_000):
    counts[sample(probs, random.random())] += 1
print("frequencies:", [c / 10_000 for c in counts], "vs", probs)
