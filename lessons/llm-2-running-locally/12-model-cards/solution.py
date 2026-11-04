def head_dim(config):
    return config.get("head_dim", config["hidden_size"] // config["num_attention_heads"])


def estimate_params(config):
    h = config["hidden_size"]
    hd = head_dim(config)
    q = h * config["num_attention_heads"] * hd
    kv = h * config["num_key_value_heads"] * hd
    attention = q + 2 * kv + q  # Q + K + V + O for one layer
    mlp = 3 * h * config["intermediate_size"]  # gate + up + down for one layer
    total = config["num_hidden_layers"] * (attention + mlp)
    embeddings = config["vocab_size"] * h
    total += embeddings if config["tie_word_embeddings"] else 2 * embeddings
    return total


def kv_bytes_per_token(config):
    return 2 * config["num_hidden_layers"] * config["num_key_value_heads"] * head_dim(config) * 2


llama31_8b = {"hidden_size": 4096, "num_hidden_layers": 32, "num_attention_heads": 32,
              "num_key_value_heads": 8, "intermediate_size": 14336, "vocab_size": 128256,
              "max_position_embeddings": 131072, "tie_word_embeddings": False}
print(f"{estimate_params(llama31_8b) / 1e9:.2f}B parameters")
print(kv_bytes_per_token(llama31_8b), "KV bytes per token")
