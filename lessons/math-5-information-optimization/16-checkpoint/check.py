import math
ev = ns.get("evaluate")
assert ev, "Keep evaluate."
r = ev([[2, 1, 0], [0, 3, 0], [1, 1, 1]], [0, 1, 2])
assert isinstance(r, dict) and set(r) >= {"loss", "ppl", "entropy"}, f"Return a dict with loss, ppl, entropy; got {r!r}."
sm = lambda z: [math.exp(v) / sum(math.exp(u) for u in z) for v in z]
want = -(math.log(sm([2, 1, 0])[0]) + math.log(sm([0, 3, 0])[1]) + math.log(1 / 3)) / 3
assert abs(r["loss"] - want) < 1e-9, f"loss should be {want:.4f}, got {r['loss']!r}."
assert abs(r["ppl"] - math.exp(want)) < 1e-9, "ppl = e^loss."
went = sum(-sum(p * math.log(p) for p in sm(z)) for z in ([2, 1, 0], [0, 3, 0], [1, 1, 1])) / 3
assert abs(r["entropy"] - went) < 1e-9, f"entropy should be {went:.4f} nats, got {r['entropy']!r}."
r = ev([[0, -1000]], [0])
assert abs(r["loss"]) < 1e-9 and abs(r["ppl"] - 1) < 1e-9, "Logits (0, −1000) must not crash: use log-sum-exp."
r = ev([[1000, 0]], [1])
assert abs(r["loss"] - 1000) < 1e-6 and r["ppl"] == math.inf, "Confidently wrong: loss 1000, perplexity math.inf, and no overflow."
