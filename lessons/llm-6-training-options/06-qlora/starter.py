def module_shapes(config):
    # h = config["hidden_size"]
    # head_dim = h // config["num_attention_heads"]
    # kv = config["num_key_value_heads"] * head_dim
    # i = config["intermediate_size"]
    # shapes = {}
    # shapes["q_proj"] = (h, h)
    # shapes["k_proj"] = (h, kv)
    # shapes["v_proj"] = (h, kv)
    # shapes["o_proj"] = (h, h)
    # shapes["gate_proj"] = (h, i)
    # shapes["up_proj"] = (h, i)
    # shapes["down_proj"] = (i, h)
    # return shapes
    return {}


def lora_trainable(config, r, targets):
    # shapes = module_shapes(config)
    # per_layer = 0
    # for t in targets:
    #     d_in, d_out = shapes[t]
    #     per_layer = per_layer + r * (d_in + d_out)
    # return per_layer * config["num_hidden_layers"]
    return 0


llama31_8b = {"hidden_size": 4096, "num_hidden_layers": 32, "num_attention_heads": 32,
              "num_key_value_heads": 8, "intermediate_size": 14336}
attention = ["q_proj", "k_proj", "v_proj", "o_proj"]
everything = attention + ["gate_proj", "up_proj", "down_proj"]
for name, targets in [("attention only", attention), ("all seven", everything)]:
    n = lora_trainable(llama31_8b, 16, targets)
    print(f"r=16, {name}: {n:,} trainable ({n / 8.03e9:.2%} of 8.03B)")
