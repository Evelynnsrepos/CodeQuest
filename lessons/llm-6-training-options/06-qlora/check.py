ms, lt = ns.get("module_shapes"), ns.get("lora_trainable")
assert ms and lt, "Keep module_shapes and lora_trainable."
cfg = {"hidden_size": 64, "num_hidden_layers": 2, "num_attention_heads": 4, "num_key_value_heads": 2, "intermediate_size": 128}
s = ms(cfg)
want = {"q_proj": (64, 64), "k_proj": (64, 32), "v_proj": (64, 32), "o_proj": (64, 64),
        "gate_proj": (64, 128), "up_proj": (64, 128), "down_proj": (128, 64)}
assert s == want, f"module_shapes returned {s!r}, expected {want!r}."
assert lt(cfg, 4, ["q_proj"]) == 4 * 128 * 2, f"lora_trainable(cfg, 4, ['q_proj']) should be 4·(64+64)·2 layers = 1024, got {lt(cfg, 4, ['q_proj'])!r}."
assert lt(cfg, 8, list(want)) == 8 * (128 + 96 + 96 + 128 + 192 + 192 + 192) * 2, "lora_trainable over all seven modules is wrong."
llama = {"hidden_size": 4096, "num_hidden_layers": 32, "num_attention_heads": 32, "num_key_value_heads": 8, "intermediate_size": 14336}
assert lt(llama, 16, list(want)) == 41943040, f"Llama 3.1 8B, r=16, all seven modules should give 41,943,040, got {lt(llama, 16, list(want)):,}."
