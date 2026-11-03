import math
f = ns.get("attend")
assert f, "Keep the function attend."
got = f([1.0, 0.0], [[1.0, 0.0], [1.0, 0.0]], [[2.0, 0.0], [0.0, 4.0]])
assert all(abs(a - b) < 1e-9 for a, b in zip(got, [1.0, 2.0])), f"Two identical keys should get equal weights, so the output is the average of the values [1.0, 2.0]. Got {got!r}."
q, keys, values = [1.0, 1.0, 1.0, 1.0], [[1.0, 1.0, 1.0, 1.0], [0.0, 0.0, 0.0, 0.0]], [[1.0], [0.0]]
got = f(q, keys, values)[0]
want = math.exp(2) / (math.exp(2) + 1)  # score 4/√4 = 2 vs 0
assert abs(got - want) < 1e-9, f"With d = 4 the first score is 4 / √4 = 2 and the second 0, so the output should be about {want:.3f}, got {got:.3f}. Did you divide by math.sqrt(len(q))?"
