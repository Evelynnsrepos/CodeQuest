import math


def train_flops(n_params, tokens):
    # return 6 * n_params * tokens
    return 0


def chinchilla_tokens(n_params):
    # return 20 * n_params
    return 0


def start_loss(vocab):
    # return math.log(vocab)
    return 0


def init_ok(first_loss, vocab):
    # return abs(first_loss - start_loss(vocab)) <= 1.0
    return False


def advantages(rewards):
    # n = len(rewards)
    # mean = sum(rewards) / n
    # total = 0
    # for r in rewards:
    #     total = total + (r - mean) ** 2
    # std = math.sqrt(total / n)
    # if std == 0:
    #     return [0.0] * n
    # out = []
    # for r in rewards:
    #     out.append((r - mean) / std)
    # return out
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
