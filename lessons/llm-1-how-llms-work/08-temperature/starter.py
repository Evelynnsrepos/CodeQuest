import math


def softmax(logits):
    m = max(logits)
    exps = [math.exp(z - m) for z in logits]
    total = sum(exps)
    return [e / total for e in exps]


def softmax_t(logits, T):
    scaled = []
    # divide every logit by T
    return softmax(logits)


tokens = [" Paris", " Lyon", " a", " the"]
logits = [9.1, 5.2, 4.0, 3.5]
for T in [0.2, 1.0, 3.0]:
    probs = softmax_t(logits, T)
    print(f"T={T}: " + "  ".join(f"{t!r} {p:.2f}" for t, p in zip(tokens, probs)))

code_temperature = ""  # "low" or "high"
