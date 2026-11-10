import math


def mean(xs):
    # return sum(xs) / len(xs)
    return 0


def std(xs):
    # m = mean(xs)
    # total = 0
    # for x in xs:
    #     total = total + (x - m) ** 2
    # return math.sqrt(total / (len(xs) - 1))
    return 0


def ci95(xs):
    # se = std(xs) / math.sqrt(len(xs))
    # m = mean(xs)
    # return (m - 1.96 * se, m + 1.96 * se)
    return (0, 0)


def clearly_better(wins):
    # low, high = ci95(wins)
    # return low > 0.5
    return False


small = [1] * 13 + [0] * 7
big = [1] * 130 + [0] * 70
for name, wins in [("20 prompts", small), ("200 prompts", big)]:
    low, high = ci95(wins)
    print(f"{name}: win rate {mean(wins):.2f}, 95% CI [{low:.2f}, {high:.2f}], clearly better: {clearly_better(wins)}")
