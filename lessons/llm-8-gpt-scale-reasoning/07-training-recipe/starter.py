import math


def initial_loss(vocab):
    return 0.0


def lr_at(step, max_lr, min_lr, warmup, total):
    return max_lr


print("loss at start for GPT-2's vocab:", round(initial_loss(50257), 3))
for step in [0, 99, 100, 1000, 5000, 9999, 10000, 12000]:
    print(step, f"{lr_at(step, 6e-4, 6e-5, 100, 10000):.2e}")
