def head_dim(config):
    return 0


def estimate_params(config):
    h = config["hidden_size"]
    hd = head_dim(config)
    attention = 0  # Q + K + V + O for one layer
    mlp = 0  # gate + up + down for one layer
    total = 0
    return total


def kv_bytes_per_token(config):
    return 0


llama31_8b = {"hidden_size": 4096, "num_hidden_layers": 32, "num_attention_heads": 32,
              "num_key_value_heads": 8, "intermediate_size": 14336, "vocab_size": 128256,
              "max_position_embeddings": 131072, "tie_word_embeddings": False}
print(f"{estimate_params(llama31_8b) / 1e9:.2f}B parameters")
print(kv_bytes_per_token(llama31_8b), "KV bytes per token")
