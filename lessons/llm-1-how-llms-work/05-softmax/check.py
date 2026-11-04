import math
f = ns.get("softmax")
assert f, "Keep the function softmax."
def close(a, b): return len(a) == len(b) and all(abs(x - y) < 1e-6 for x, y in zip(a, b))
got = f([0.0, 0.0])
assert close(got, [0.5, 0.5]), f"softmax([0, 0]) returned {got!r}, expected [0.5, 0.5]: equal logits give equal probabilities."
got = f([1.0, 2.0, 3.0])
want = [math.exp(1) / (math.exp(1) + math.exp(2) + math.exp(3)), math.exp(2) / (math.exp(1) + math.exp(2) + math.exp(3)), math.exp(3) / (math.exp(1) + math.exp(2) + math.exp(3))]
assert close(got, want), f"softmax([1, 2, 3]) returned {got!r}, expected about {[round(w, 4) for w in want]}."
assert abs(sum(got) - 1) < 1e-9, "The probabilities should add up to 1."
try:
    got = f([1000.0, 1001.0])
except OverflowError:
    raise AssertionError("softmax([1000, 1001]) overflowed. Subtract the largest logit before calling math.exp.")
assert close(got, [1 / (1 + math.e), math.e / (1 + math.e)]), f"softmax([1000, 1001]) returned {got!r}, expected about [0.269, 0.731]."
