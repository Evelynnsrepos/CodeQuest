import math


def softmax(logits):
    m = max(logits)
    exps = []
    for z in logits:
        exps.append(math.exp(z - m))
    total = sum(exps)
    probs = []
    for e in exps:
        probs.append(e / total)
    return probs


def softmax_t(logits, T):
    scaled = []
    for z in logits:
        scaled.append(z / T)
    return softmax(scaled)


tokens = [" Paris", " Lyon", " a", " the"]
logits = [9.1, 5.2, 4.0, 3.5]
for T in [0.2, 1.0, 3.0]:
    probs = softmax_t(logits, T)
    print("T =", T)
    for i in range(len(tokens)):
        print("   ", tokens[i], round(probs[i], 2))

code_temperature = "low"
