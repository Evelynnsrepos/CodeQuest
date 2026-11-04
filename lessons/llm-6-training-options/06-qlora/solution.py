def module_shapes(config):
    h = config["hidden_size"]
    hd = h // config["num_attention_heads"]
    kv = config["num_key_value_heads"] * hd
    i = config["intermediate_size"]
    return {"q_proj": (h, h), "k_proj": (h, kv), "v_proj": (h, kv), "o_proj": (h, h),
            "gate_proj": (h, i), "up_proj": (h, i), "down_proj": (i, h)}


def lora_trainable(config, r, targets):
    shapes = module_shapes(config)
    per_layer = sum(r * (shapes[t][0] + shapes[t][1]) for t in targets)
    return per_layer * config["num_hidden_layers"]


llama31_8b = {"hidden_size": 4096, "num_hidden_layers": 32, "num_attention_heads": 32,
              "num_key_value_heads": 8, "intermediate_size": 14336}
attention = ["q_proj", "k_proj", "v_proj", "o_proj"]
everything = attention + ["gate_proj", "up_proj", "down_proj"]
for name, targets in [("attention only", attention), ("all seven", everything)]:
    n = lora_trainable(llama31_8b, 16, targets)
    print(f"r=16, {name}: {n:,} trainable ({n / 8.03e9:.2%} of 8.03B)")
