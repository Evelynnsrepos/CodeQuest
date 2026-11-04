import math


def initial_loss(vocab):
    return math.log(vocab)


def lr_at(step, max_lr, min_lr, warmup, total):
    if step < warmup:
        return max_lr * (step + 1) / warmup
    if step >= total:
        return min_lr
    r = (step - warmup) / (total - warmup)
    return min_lr + 0.5 * (1 + math.cos(math.pi * r)) * (max_lr - min_lr)


print("loss at start for GPT-2's vocab:", round(initial_loss(50257), 3))
for step in [0, 99, 100, 1000, 5000, 9999, 10000, 12000]:
    print(step, f"{lr_at(step, 6e-4, 6e-5, 100, 10000):.2e}")
