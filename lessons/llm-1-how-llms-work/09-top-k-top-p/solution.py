def renormalize(kept):
    total = sum(kept.values())
    return {token: p / total for token, p in kept.items()}


def top_k(probs, k):
    ranked = sorted(probs.items(), key=lambda pair: pair[1], reverse=True)
    kept = {}
    for token, q in ranked[:k]:
        kept[token] = q
    return renormalize(kept)


def top_p(probs, p):
    ranked = sorted(probs.items(), key=lambda pair: pair[1], reverse=True)
    kept, running = {}, 0
    for token, q in ranked:
        kept[token] = q
        running += q
        if running >= p:
            break
    return renormalize(kept)


probs = {" Paris": 0.60, " Lyon": 0.25, " Nice": 0.10, " a": 0.04, " the": 0.01}
print({t: round(q, 2) for t, q in top_k(probs, 2).items()})
print({t: round(q, 2) for t, q in top_p(probs, 0.9).items()})
