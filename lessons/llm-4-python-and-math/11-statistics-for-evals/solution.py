import math


def mean(xs):
    return sum(xs) / len(xs)


def std(xs):
    m = mean(xs)
    return math.sqrt(sum((x - m) ** 2 for x in xs) / (len(xs) - 1))


def ci95(xs):
    se = std(xs) / math.sqrt(len(xs))
    return (mean(xs) - 1.96 * se, mean(xs) + 1.96 * se)


def clearly_better(wins):
    return ci95(wins)[0] > 0.5


small = [1] * 13 + [0] * 7
big = [1] * 130 + [0] * 70
for name, wins in [("20 prompts", small), ("200 prompts", big)]:
    low, high = ci95(wins)
    print(f"{name}: win rate {mean(wins):.2f}, 95% CI [{low:.2f}, {high:.2f}], clearly better: {clearly_better(wins)}")
