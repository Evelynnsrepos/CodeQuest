import math
t, p = ns.get("total_log_prob"), ns.get("perplexity")
assert t and p, "Keep the functions total_log_prob and perplexity."
got = t([0.5, 0.5])
assert abs(got - 2 * math.log(0.5)) < 1e-9, f"total_log_prob([0.5, 0.5]) returned {got!r}, expected {2 * math.log(0.5):.4f} (log 0.5 + log 0.5)."
got = p([1.0, 1.0, 1.0])
assert abs(got - 1.0) < 1e-9, f"perplexity([1, 1, 1]) returned {got!r}, expected 1.0: a model that is always certain and right."
got = p([0.1, 0.02, 0.3])
want = math.exp(-(math.log(0.1) + math.log(0.02) + math.log(0.3)) / 3)
assert abs(got - want) < 1e-9, f"perplexity([0.1, 0.02, 0.3]) returned {got!r}, expected about {want:.3f}. Divide by the number of tokens."
