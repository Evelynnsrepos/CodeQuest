def renormalize(kept):
    total = sum(kept.values())
    return {token: p / total for token, p in kept.items()}


def top_k(probs, k):
    ranked = sorted(probs.items(), key=lambda pair: pair[1], reverse=True)
    kept = {}
    # put the first k pairs of ranked into kept
    return renormalize(kept)


def top_p(probs, p):
    ranked = sorted(probs.items(), key=lambda pair: pair[1], reverse=True)
    kept, running = {}, 0
    # keep tokens until running >= p
    return renormalize(kept)


probs = {" Paris": 0.60, " Lyon": 0.25, " Nice": 0.10, " a": 0.04, " the": 0.01}
print({t: round(q, 2) for t, q in top_k(probs, 2).items()})
print({t: round(q, 2) for t, q in top_p(probs, 0.9).items()})
