import math


def train_flops(n_params, tokens):
    return 0


def chinchilla_tokens(n_params):
    return 0


def start_loss(vocab):
    return 0


def init_ok(first_loss, vocab):
    return False


def advantages(rewards):
    return []


print(train_flops(7e9, 2e12), chinchilla_tokens(7e9), start_loss(32000), init_ok(31.5, 32000))
print(advantages([1, 0, 0, 1]), advantages([1, 1, 1]))


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
