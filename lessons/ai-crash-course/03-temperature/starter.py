import math


def softmax_t(scores, t):
    # Step 1: scaled = []   then   for s in scores:   inside: scaled.append(s / t)
    # Step 2: biggest = max(scaled)
    # Step 3: exps = []     then   for s in scaled:   inside: exps.append(math.exp(s - biggest))
    # Step 4: total = sum(exps)
    #         probs = []    then   for e in exps:     inside: probs.append(e / total)
    #         return probs
    return scores


# These lines just show your result rounded to 2 decimals. You don't need to change them.
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 1)])
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 0.2)])
print([round(p, 2) for p in softmax_t([2.0, 1.0, 0.1], 5)])
