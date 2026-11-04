def rrf(rankings, k=60):
    score = {}
    for ranking in rankings:
        for rank, doc in enumerate(ranking, 1):
            score[doc] = score.get(doc, 0) + 1 / (k + rank)
    return sorted(score, key=lambda d: (-score[d], d))


def rerank(query, candidates, scorer, top=3):
    return sorted(candidates, key=lambda c: -scorer(query, c["text"]))[:top]


def overlap_scorer(query, text):
    q = set(query.lower().split())
    t = set(text.lower().split())
    return len(q & t) / len(q) if q else 0.0


print(rrf([["a", "b", "c"], ["c", "a", "d"]]))
cands = [{"text": "nix flakes pin inputs"}, {"text": "delete old nix generations with nix-collect-garbage"}]
print(rerank("delete old generations", cands, overlap_scorer, top=1))
