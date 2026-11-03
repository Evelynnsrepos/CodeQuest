import math


def mean(xs):
    return 0


def std(xs):
    return 0


def ci95(xs):
    return (0, 0)


def clearly_better(wins):
    return False


small = [1] * 13 + [0] * 7
big = [1] * 130 + [0] * 70
for name, wins in [("20 prompts", small), ("200 prompts", big)]:
    low, high = ci95(wins)
    print(f"{name}: win rate {mean(wins):.2f}, 95% CI [{low:.2f}, {high:.2f}], clearly better: {clearly_better(wins)}")
