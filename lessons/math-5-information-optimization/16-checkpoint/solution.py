import math


def log_softmax(z):
    m = max(z)
    lse = m + math.log(sum(math.exp(v - m) for v in z))
    return [v - lse for v in z]


def evaluate(logits_list, targets):
    n = len(targets)
    loss = ent = 0.0
    for z, y in zip(logits_list, targets):
        lp = log_softmax(z)
        loss -= lp[y] / n
        ent -= sum(math.exp(l) * l for l in lp) / n
    return {"loss": loss, "ppl": math.exp(loss) if loss < 709 else math.inf, "entropy": ent}


print(evaluate([[2, 1, 0], [0, 3, 0], [1, 1, 1]], [0, 1, 2]))
