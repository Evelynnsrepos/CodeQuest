rb, re_, rh, rep, IDS, GOLDEN = (ns.get(n) for n in ("rank_bm25", "rank_embed", "rank_hybrid", "report", "IDS", "GOLDEN"))
assert rb and re_ and rh and rep and IDS and GOLDEN, "Keep rank_bm25, rank_embed, rank_hybrid, report, IDS and GOLDEN."
q = "which port does the ollama api use"
for f in (rb, re_, rh):
    r = f(q)
    assert sorted(r) == sorted(IDS), f"{f.__name__} must return a full ranking of all note ids."
assert rb(q)[0] == "ollama-api", "BM25 should put ollama-api first for that question."
r = rep()
assert set(r) == {"bm25", "embed", "hybrid"} and all(set(v) == {"recall@3", "mrr"} for v in r.values()), f"report() layout. Got {r!r}."
for name in r:
    res = {qq: {"bm25": rb, "embed": re_, "hybrid": rh}[name](qq) for qq, _ in GOLDEN}
    want = sum(g in res[qq][:3] for qq, g in GOLDEN) / len(GOLDEN)
    assert abs(r[name]["recall@3"] - want) < 1e-9, f"{name} recall@3 should be {want:.3f}."
h = r["hybrid"]["recall@3"]
assert h >= 0.9, f"Hybrid recall@3 should be at least 0.9, got {h:.2f}."
assert h >= max(r["bm25"]["recall@3"], r["embed"]["recall@3"]), "Hybrid should be at least as good as the better single method."
