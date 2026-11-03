f = ns.get("softmax_t")
assert f, "Keep the function softmax_t."
logits = [2.0, 1.0, 0.0]
base = ns["softmax"](logits)
got = f(logits, 1.0)
assert all(abs(a - b) < 1e-9 for a, b in zip(got, base)), "softmax_t(logits, 1.0) should be exactly softmax(logits)."
cold, hot = f(logits, 0.5), f(logits, 2.0)
assert abs(cold[0] - ns["softmax"]([4.0, 2.0, 0.0])[0]) < 1e-9, f"softmax_t([2, 1, 0], 0.5) returned {cold!r}. Dividing by 0.5 should give the same result as softmax([4, 2, 0])."
assert cold[0] > base[0] > hot[0], "A lower temperature should give the top token more probability, a higher temperature less."
assert ns.get("code_temperature") == "low", "Code has to be exactly right, so you want the model's most likely tokens. Set code_temperature to \"low\" or \"high\"."
