def module_shapes(config):
    return {}


def lora_trainable(config, r, targets):
    return 0


llama31_8b = {"hidden_size": 4096, "num_hidden_layers": 32, "num_attention_heads": 32,
              "num_key_value_heads": 8, "intermediate_size": 14336}
attention = ["q_proj", "k_proj", "v_proj", "o_proj"]
everything = attention + ["gate_proj", "up_proj", "down_proj"]
for name, targets in [("attention only", attention), ("all seven", everything)]:
    n = lora_trainable(llama31_8b, 16, targets)
    print(f"r=16, {name}: {n:,} trainable ({n / 8.03e9:.2%} of 8.03B)")
