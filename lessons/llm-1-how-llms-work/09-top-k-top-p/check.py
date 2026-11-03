k, p = ns.get("top_k"), ns.get("top_p")
assert k and p, "Keep the functions top_k and top_p."
probs = {"a": 0.5, "b": 0.3, "c": 0.15, "d": 0.05}
def close(got, want): return set(got) == set(want) and all(abs(got[t] - want[t]) < 1e-9 for t in want)
try:
    got = k(probs, 2)
except ZeroDivisionError:
    raise AssertionError("top_k kept nothing, so renormalize divided by zero. Put the first k pairs into kept.")
assert close(got, {"a": 0.625, "b": 0.375}), f"top_k(probs, 2) returned {got!r}, expected {{'a': 0.625, 'b': 0.375}}."
assert close(k(probs, 1), {"a": 1.0}), "top_k(probs, 1) should keep only the top token, with probability 1.0."
try:
    got = p(probs, 0.75)
except ZeroDivisionError:
    raise AssertionError("top_p kept nothing, so renormalize divided by zero.")
assert close(got, {"a": 0.625, "b": 0.375}), f"top_p(probs, 0.75) returned {got!r}, expected {{'a': 0.625, 'b': 0.375}}: 0.5 + 0.3 = 0.8 is the first total ≥ 0.75."
assert close(p(probs, 0.4), {"a": 1.0}), "top_p(probs, 0.4) should keep only 'a': 0.5 alone is already ≥ 0.4."
got = p(probs, 1.0)
assert len(got) == 4, f"top_p(probs, 1.0) should keep all four tokens, got {sorted(got)}."
