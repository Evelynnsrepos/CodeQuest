def head_dim(config):
    if "head_dim" in config:
        return config["head_dim"]
    return config["hidden_size"] // config["num_attention_heads"]


def estimate_params(config):
    h = config["hidden_size"]
    hd = head_dim(config)
    q = h * config["num_attention_heads"] * hd
    kv = h * config["num_key_value_heads"] * hd
    attention = q + kv + kv + q
    mlp = 3 * h * config["intermediate_size"]
    total = config["num_hidden_layers"] * (attention + mlp)
    embeddings = config["vocab_size"] * h
    if config["tie_word_embeddings"]:
        total = total + embeddings
    else:
        total = total + 2 * embeddings
    return total


def kv_bytes_per_token(config):
    return 2 * config["num_hidden_layers"] * config["num_key_value_heads"] * head_dim(config) * 2


llama31_8b = {"hidden_size": 4096, "num_hidden_layers": 32, "num_attention_heads": 32,
              "num_key_value_heads": 8, "intermediate_size": 14336, "vocab_size": 128256,
              "max_position_embeddings": 131072, "tie_word_embeddings": False}
print(round(estimate_params(llama31_8b) / 1000000000, 2), "billion parameters")
print(kv_bytes_per_token(llama31_8b), "KV bytes per token")
