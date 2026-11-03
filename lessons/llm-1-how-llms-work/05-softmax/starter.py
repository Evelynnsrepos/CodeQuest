import math


def softmax(logits):
    m = 0  # the largest logit
    exps = []
    # fill exps with math.exp(z - m) for every z in logits
    total = 0
    probs = []
    # divide every entry of exps by total
    return probs


tokens = [" Paris", " Lyon", " a", " the"]
logits = [9.1, 5.2, 4.0, 3.5]
for token, p in zip(tokens, softmax(logits)):
    print(f"{token!r:10} {p:.3f}")
