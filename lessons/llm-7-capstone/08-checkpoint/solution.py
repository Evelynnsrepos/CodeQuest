import math


def fits(params_b, bits, vram_gb, overhead_gb=1.5):
    return params_b * bits / 8 + overhead_gb <= vram_gb


def full_ft_gb(params_b):
    return params_b * 16


def best_step(log):
    return min(log, key=lambda pair: pair[1])[0]


def win_interval(wins, n):
    p = wins / n
    e = 1.96 * math.sqrt(p * (1 - p) / n)
    return (p - e, p + e)


def clear_win(wins, n):
    return win_interval(wins, n)[0] > 0.5


print(fits(8, 16, 12), fits(8, 4.5, 12), full_ft_gb(8), best_step([(200, 1.9), (400, 1.6), (600, 1.5), (800, 1.7)]))
print(win_interval(60, 100), clear_win(60, 100), clear_win(55, 100))


ANSWERS = {
    1: "b",
    2: "c",
    3: "d",
    4: "a",
    5: "c",
    6: "b",
}

for q, a in ANSWERS.items():
    print(q, a or "(not answered)")
