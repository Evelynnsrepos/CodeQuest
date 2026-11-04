import math
g, mb, mv, rn = ns.get("gelu"), ns.get("mlp_block"), ns["matvec"], ns["rms_norm"]
assert g and mb, "Keep gelu and mlp_block."
assert abs(g(0.0)) < 1e-12, "gelu(0) should be 0."
assert abs(g(1.0) - 0.8411919906) < 1e-6, f"gelu(1.0) should be about 0.8412, got {g(1.0)!r}."
assert abs(g(-3.0) - (-0.0036373920)) < 1e-6, f"gelu(-3.0) should be about -0.0036 (almost 0, like ReLU), got {g(-3.0)!r}."
W1 = [[1.0, 2.0], [-1.0, 0.5], [0.3, 0.3]]
W2 = [[1.0, 0.0, 1.0], [0.0, -1.0, 2.0]]
x = [0.5, -2.0]
want = [a + b for a, b in zip(x, mv(W2, [0.5 * v * (1 + math.tanh(math.sqrt(2 / math.pi) * (v + 0.044715 * v ** 3))) for v in mv(W1, rn(x))]))]
got = mb(x, W1, W2)
assert len(got) == 2 and all(abs(a - b) < 1e-9 for a, b in zip(got, want)), f"mlp_block should be x + W2·gelu(W1·rms_norm(x)); expected {want!r}, got {got!r}."
zero = mb([1.0, 2.0], [[0.0, 0.0]], [[0.0], [0.0]])
assert all(abs(a - b) < 1e-12 for a, b in zip(zero, [1.0, 2.0])), "With all-zero weights the block should return x unchanged (that's the residual connection)."
