import math
f = ns.get
for name in ("train_flops", "chinchilla_tokens", "start_loss", "init_ok", "advantages"):
    assert f(name), f"Keep the function {name}."
assert abs(f("train_flops")(7e9, 2e12) - 8.4e22) < 1e18, "train_flops: 6 · N · D. 7e9 params on 2e12 tokens = 8.4e22."
assert abs(f("chinchilla_tokens")(7e9) - 1.4e11) < 1e6, "chinchilla_tokens: 20 per parameter."
assert abs(f("start_loss")(32000) - math.log(32000)) < 1e-9, "start_loss: natural log of the vocabulary size (≈ 10.37)."
assert f("init_ok")(31.5, 32000) is False and f("init_ok")(10.6, 32000) is True, "init_ok: within 1.0 of ln(vocab)."
a = f("advantages")([1, 0, 0, 1])
assert len(a) == 4 and all(abs(x - y) < 1e-9 for x, y in zip(a, [1, -1, -1, 1])), f"advantages([1,0,0,1]) = [1, -1, -1, 1], got {a!r}."
a = f("advantages")([1, 1, 1])
assert list(a) == [0, 0, 0], "All rewards equal: no signal, all zeros (and no division by zero)."

A = ns.get("ANSWERS")
assert isinstance(A, dict), "Keep the ANSWERS dict."
key = {1: 'b', 2: 'c', 3: 'd', 4: 'a', 5: 'b', 6: 'c'}
hint = {1: 'what does the + in x = x + f(x) do to the gradient?', 2: 'what part of RoPE depends on position?', 3: 'think about cost at inference, not training', 4: 'which stage shards the weights too?', 5: "Goodhart's law", 6: 'compute ln(vocab)'}
for q in key:
    got = str(A.get(q, "")).strip().lower()
    assert got, f"Question {q} has no answer yet."
    assert got in "abcd" and len(got) == 1, f"Question {q}: answer with one letter, a to d."
    assert got == key[q], f"Question {q} isn't right. Hint: {hint[q]}."
