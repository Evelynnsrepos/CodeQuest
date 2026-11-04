hd, ep, kv = ns.get("head_dim"), ns.get("estimate_params"), ns.get("kv_bytes_per_token")
assert hd and ep and kv, "Keep head_dim, estimate_params and kv_bytes_per_token."
llama = {"hidden_size": 4096, "num_hidden_layers": 32, "num_attention_heads": 32, "num_key_value_heads": 8,
         "intermediate_size": 14336, "vocab_size": 128256, "tie_word_embeddings": False}
qwen = {"hidden_size": 4096, "num_hidden_layers": 36, "num_attention_heads": 32, "num_key_value_heads": 8, "head_dim": 128,
        "intermediate_size": 12288, "vocab_size": 151936, "tie_word_embeddings": False}
small = {"hidden_size": 2048, "num_hidden_layers": 28, "num_attention_heads": 16, "num_key_value_heads": 8, "head_dim": 128,
         "intermediate_size": 6144, "vocab_size": 151936, "tie_word_embeddings": True}
assert hd(llama) == 128, f"head_dim(llama) returned {hd(llama)!r}, expected 4096 // 32 = 128."
assert hd({"hidden_size": 2560, "num_attention_heads": 32, "head_dim": 128}) == 128, "When the config has head_dim, use it instead of computing it."
got = ep(llama)
assert got == 8029995008, f"estimate_params(Llama 3.1 8B) returned {got!r}, expected 8,029,995,008 (about 8.03B)."
got = ep(qwen)
assert got == 8190427136, f"estimate_params(Qwen3-8B) returned {got!r}, expected 8,190,427,136 (about 8.19B)."
got = ep(small)
assert got == 1720451072, f"estimate_params with tie_word_embeddings true returned {got!r}, expected 1,720,451,072: count the embedding table only once."
assert kv(llama) == 131072, f"kv_bytes_per_token(llama) returned {kv(llama)!r}, expected 131072."
assert kv(qwen) == 147456, f"kv_bytes_per_token(qwen) returned {kv(qwen)!r}, expected 147456 (36 layers)."
