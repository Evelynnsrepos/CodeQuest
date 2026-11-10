import math


def softmax(logits):
    m = 0  # change 0 to: max(logits)
    exps = []
    # for z in logits:
    #     exps.append(math.exp(z - m))
    total = 0  # change 0 to: sum(exps)
    probs = []
    # for e in exps:
    #     probs.append(e / total)
    return probs


tokens = [" Paris", " Lyon", " a", " the"]
logits = [9.1, 5.2, 4.0, 3.5]
probs = softmax(logits)
for i in range(len(tokens)):
    print(tokens[i], round(probs[i], 3))
