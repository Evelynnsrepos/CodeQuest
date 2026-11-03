f = ns.get("gpt_forward")
assert f, "Keep gpt_forward."
dot, mv, sm, rn, ge, rp, ca, rpms = (ns[k] for k in ["dot", "matvec", "softmax", "rms_norm", "gelu", "rope", "causal_attention", "random_params"])
def ref(tokens, P):
    x = [list(P["wte"][t]) for t in tokens]
    for L in P["layers"]:
        h = [rn(r) for r in x]
        a = ca([rp(mv(L["Wq"], r), i) for i, r in enumerate(h)], [rp(mv(L["Wk"], r), i) for i, r in enumerate(h)], [mv(L["Wv"], r) for r in h])
        x = [[u + v for u, v in zip(xi, mv(L["Wo"], ai))] for xi, ai in zip(x, a)]
        x = [[u + v for u, v in zip(xi, mv(L["W2"], [ge(z) for z in mv(L["W1"], rn(xi))]))] for xi in x]
    return sm([dot(row, rn(x[-1])) for row in P["wte"]])
P = rpms(7, 4, 2, seed=3)
got = f([1, 4, 2, 6], P)
assert isinstance(got, list) and len(got) == 7, f"Return one probability per vocabulary token (7), got {got!r}."
assert abs(sum(got) - 1) < 1e-9, "The probabilities should sum to 1."
want = ref([1, 4, 2, 6], P)
assert all(abs(a - b) < 1e-9 for a, b in zip(got, want)), "The numbers don't match a reference GPT. Check: RMSNorm before each sub-layer, RoPE on Q and K (not V) with each row's position, both residual additions, final RMSNorm on the last position."
