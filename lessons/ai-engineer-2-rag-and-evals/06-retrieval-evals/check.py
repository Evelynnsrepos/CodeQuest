rk, mr, br, NOTES, GOLDEN = (ns.get(n) for n in ("recall_at_k", "mrr", "bm25_results", "NOTES", "GOLDEN"))
assert rk and mr and br and NOTES and GOLDEN, "Keep recall_at_k, mrr, bm25_results, NOTES and GOLDEN."
res = {"q1": ["a", "b", "c"], "q2": ["c", "b", "a"], "q3": ["b", "c", "d"]}
gold = [("q1", "a"), ("q2", "a"), ("q3", "x")]
assert abs(rk(res, gold, 1) - 1 / 3) < 1e-9 and abs(rk(res, gold, 3) - 2 / 3) < 1e-9, "recall@k: share of questions with the right id in the top k."
assert abs(mr(res, gold) - (1 + 1 / 3 + 0) / 3) < 1e-9, "MRR: average of 1/rank, 0 when missing."
r = br(NOTES, GOLDEN)
assert set(r) == {q for q, _ in GOLDEN} and all(len(v) == len(NOTES) for v in r.values()), "bm25_results: a full ranking of note ids per question."
assert rk(r, GOLDEN, 3) >= 0.6, f"BM25 should get recall@3 ≥ 0.6 here, got {rk(r, GOLDEN, 3):.2f}."
