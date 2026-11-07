def rrf(rankings, k=60):
    score = {}
    for ranking in rankings:
        rank = 1
        for doc in ranking:
            score[doc] = score.get(doc, 0) + 1 / (k + rank)
            rank = rank + 1
    ids = sorted(score)
    out = []
    for step in range(len(ids)):
        best = None
        for doc in ids:
            if doc not in out:
                if best is None or score[doc] > score[best]:
                    best = doc
        out.append(best)
    return out


def rerank(query, candidates, scorer, top=3):
    scores = []
    for c in candidates:
        scores.append(scorer(query, c["text"]))
    picked = []
    for step in range(top):
        best = None
        for i in range(len(candidates)):
            if i not in picked:
                if best is None or scores[i] > scores[best]:
                    best = i
        if best is None:
            break
        picked.append(best)
    out = []
    for i in picked:
        out.append(candidates[i])
    return out


def overlap_scorer(query, text):
    q = set(query.lower().split())
    t = set(text.lower().split())
    if len(q) == 0:
        return 0.0
    shared = 0
    for w in q:
        if w in t:
            shared = shared + 1
    return shared / len(q)


print(rrf([["a", "b", "c"], ["c", "a", "d"]]))
cands = [{"text": "nix flakes pin inputs"}, {"text": "delete old nix generations with nix-collect-garbage"}]
print(rerank("delete old generations", cands, overlap_scorer, top=1))
