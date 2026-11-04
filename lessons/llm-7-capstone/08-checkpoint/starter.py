import math


def fits(params_b, bits, vram_gb, overhead_gb=1.5):
    return False


def full_ft_gb(params_b):
    return 0


def best_step(log):
    return None


def win_interval(wins, n):
    return (0, 0)


def clear_win(wins, n):
    return False


print(fits(8, 16, 12), fits(8, 4.5, 12), full_ft_gb(8), best_step([(200, 1.9), (400, 1.6), (600, 1.5), (800, 1.7)]))
print(win_interval(60, 100), clear_win(60, 100), clear_win(55, 100))


ANSWERS = {
    1: "",
    2: "",
    3: "",
    4: "",
    5: "",
    6: "",
}

for q, a in ANSWERS.items():
    print(q, a or "(not answered)")
