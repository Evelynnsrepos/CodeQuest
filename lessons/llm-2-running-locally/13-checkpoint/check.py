p = ns.get("predict")
assert p, "Keep the function predict."
tiny = {"hidden_size": 1000, "num_hidden_layers": 1, "num_attention_heads": 10, "num_key_value_heads": 10,
        "intermediate_size": 1000, "vocab_size": 1000, "tie_word_embeddings": True}
# 6,000,000 params; at 8 bpw = 0.006 GB; KV 4000 bytes/token
assert p(tiny, 8, 1000, 1.1) is True, "predict should return True when weights + KV + 1 GB fit in the budget."
assert p(tiny, 8, 1000, 1.0) is False, "predict should return False when weights + KV + 1 GB are more than the budget (don't forget the 1 GB)."
assert p(tiny, 8, 250_000, 2.0) is False, "With a 250,000-token context the KV cache alone is 1 GB here. Did you include it?"
for name in ("fits_a", "fits_b", "fits_c"):
    assert isinstance(ns.get(name), bool), f"Set {name} to True or False."
assert ns["fits_a"] is False, "fits_a: Qwen3-14B is about 14.8B parameters, so Q4_K_M is about 8.9 GB, plus 1.3 GB of KV cache and 1 GB overhead. Compare with 11."
assert ns["fits_b"] is True, "fits_b: about 6.6 GB of weights + 2.1 GB of KV cache + 1 GB = 9.8 GB."
assert ns["fits_c"] is True, "fits_c: IQ4_XS brings the weights to about 7.9 GB, and 4k context is only 0.7 GB."
