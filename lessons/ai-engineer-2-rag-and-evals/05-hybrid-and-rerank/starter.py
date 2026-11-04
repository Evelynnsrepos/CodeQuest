def rrf(rankings, k=60):
    return []


def rerank(query, candidates, scorer, top=3):
    return candidates[:top]


def overlap_scorer(query, text):
    return 0.0


print(rrf([["a", "b", "c"], ["c", "a", "d"]]))
cands = [{"text": "nix flakes pin inputs"}, {"text": "delete old nix generations with nix-collect-garbage"}]
print(rerank("delete old generations", cands, overlap_scorer, top=1))
