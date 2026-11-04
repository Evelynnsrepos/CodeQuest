import math
f = ns.get("causal_attention")
assert f, "Keep the function causal_attention."
X = ns["X"]; Wq = ns["Wq"]; Wk = ns["Wk"]; Wv = ns["Wv"]
out = f(X, Wq, Wk, Wv)
assert isinstance(out, list) and len(out) == 4, f"causal_attention should return one vector per position (4), got {out!r}."
V = ns["matmul"](X, Wv)
assert all(abs(a - b) < 1e-9 for a, b in zip(out[0], V[0])), f"Position 0 can only see itself, so its output must equal V[0] = {V[0]}, got {out[0]}."
X2 = [r[:] for r in X]
X2[3] = [100.0, -50.0, 7.0]
out2 = f(X2, Wq, Wk, Wv)
for t in range(3):
    assert all(abs(a - b) < 1e-9 for a, b in zip(out[t], out2[t])), f"Changing the last token changed position {t}'s output. Earlier positions must not see later ones (the causal mask)."
Q, K = ns["matmul"](X, Wq), ns["matmul"](X, Wk)
sc = [ns["dot"](Q[1], K[s]) / math.sqrt(2) for s in range(2)]
w = ns["softmax"](sc)
want = [w[0] * V[0][h] + w[1] * V[1][h] for h in range(2)]
assert all(abs(a - b) < 1e-9 for a, b in zip(out[1], want)), f"Position 1 should be {want}, got {out[1]}. Scale scores by 1/√H with H = head size."
