import math


def train_flops(n_params, tokens):
    return 6 * n_params * tokens


def chinchilla_tokens(n_params):
    return 20 * n_params


def start_loss(vocab):
    return math.log(vocab)


def init_ok(first_loss, vocab):
    return abs(first_loss - start_loss(vocab)) <= 1.0


def advantages(rewards):
    n = len(rewards)
    mean = sum(rewards) / n
    total = 0
    for r in rewards:
        total = total + (r - mean) ** 2
    std = math.sqrt(total / n)
    if std == 0:
        return [0.0] * n
    out = []
    for r in rewards:
        out.append((r - mean) / std)
    return out


print(train_flops(7e9, 2e12), chinchilla_tokens(7e9), start_loss(32000), init_ok(31.5, 32000))
print(advantages([1, 0, 0, 1]), advantages([1, 1, 1]))


ANSWERS = {
    1: "b",
    2: "c",
    3: "d",
    4: "a",
    5: "b",
    6: "c",
}

for q, a in ANSWERS.items():
    print(q, a or "(not answered)")
