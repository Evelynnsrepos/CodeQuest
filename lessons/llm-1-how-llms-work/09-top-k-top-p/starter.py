def rank(probs):
    """Given: (token, probability) pairs, most likely first."""
    return sorted(probs.items(), key=lambda pair: pair[1], reverse=True)


def renormalize(kept):
    """Given: divide every probability by the total, so they add up to 1."""
    total = sum(kept.values())
    result = {}
    for token in kept:
        result[token] = kept[token] / total
    return result


def top_k(probs, k):
    ranked = rank(probs)
    kept = {}
    # for token, q in ranked[:k]:
    #     kept[token] = q
    return renormalize(kept)


def top_p(probs, p):
    ranked = rank(probs)
    kept = {}
    running = 0
    # for token, q in ranked:
    #     kept[token] = q
    #     running = running + q
    #     if running >= p:
    #         break
    return renormalize(kept)


probs = {" Paris": 0.60, " Lyon": 0.25, " Nice": 0.10, " a": 0.04, " the": 0.01}
for token, q in top_k(probs, 2).items():
    print("top-k:", token, round(q, 2))
for token, q in top_p(probs, 0.9).items():
    print("top-p:", token, round(q, 2))
