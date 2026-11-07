def estimate_params(c):
    """Given: lesson 12's parameter estimate."""
    if "head_dim" in c:
        hd = c["head_dim"]
    else:
        hd = c["hidden_size"] // c["num_attention_heads"]
    q = c["hidden_size"] * c["num_attention_heads"] * hd
    kv = c["hidden_size"] * c["num_key_value_heads"] * hd
    per_layer = 2 * q + 2 * kv + 3 * c["hidden_size"] * c["intermediate_size"]
    emb = c["vocab_size"] * c["hidden_size"]
    if c["tie_word_embeddings"]:
        return c["num_hidden_layers"] * per_layer + emb
    return c["num_hidden_layers"] * per_layer + 2 * emb


def kv_bytes_per_token(c):
    """Given: lesson 12's KV bytes per token."""
    if "head_dim" in c:
        hd = c["head_dim"]
    else:
        hd = c["hidden_size"] // c["num_attention_heads"]
    return 2 * c["num_hidden_layers"] * c["num_key_value_heads"] * hd * 2


def predict(config, bpw, context, budget_gb):
    # weights = estimate_params(config) * bpw / 8 / 1000000000
    # kv = kv_bytes_per_token(config) * context / 1000000000
    # return weights + kv + 1.0 <= budget_gb
    return None


qwen3_14b = {"hidden_size": 5120, "num_hidden_layers": 40, "num_attention_heads": 40, "num_key_value_heads": 8,
             "head_dim": 128, "intermediate_size": 17408, "vocab_size": 151936, "tie_word_embeddings": False}
llama31_8b = {"hidden_size": 4096, "num_hidden_layers": 32, "num_attention_heads": 32, "num_key_value_heads": 8,
              "intermediate_size": 14336, "vocab_size": 128256, "tie_word_embeddings": False}

# your hand predictions first, True or False
fits_a = None
fits_b = None
fits_c = None

print("a:", predict(qwen3_14b, 4.8, 8192, 11), "you said", fits_a)
print("b:", predict(llama31_8b, 6.6, 16384, 11), "you said", fits_b)
print("c:", predict(qwen3_14b, 4.3, 4096, 11), "you said", fits_c)
