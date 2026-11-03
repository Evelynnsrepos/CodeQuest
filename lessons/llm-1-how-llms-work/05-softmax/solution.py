import math


def softmax(logits):
    m = max(logits)  # the largest logit
    exps = []
    for z in logits:
        exps.append(math.exp(z - m))
    total = sum(exps)
    probs = []
    for e in exps:
        probs.append(e / total)
    return probs


tokens = [" Paris", " Lyon", " a", " the"]
logits = [9.1, 5.2, 4.0, 3.5]
for token, p in zip(tokens, softmax(logits)):
    print(f"{token!r:10} {p:.3f}")
