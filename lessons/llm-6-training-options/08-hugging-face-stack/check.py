lc, sc = ns.get("make_lora_config"), ns.get("make_sft_config")
assert lc and sc, "Keep make_lora_config and make_sft_config."
att = ["q_proj", "k_proj", "v_proj", "o_proj"]
mlp = ["gate_proj", "up_proj", "down_proj"]
c = lc(8)
assert c == {"r": 8, "lora_alpha": 16, "lora_dropout": 0.05, "target_modules": att + mlp, "task_type": "CAUSAL_LM"}, f"make_lora_config(8) returned {c!r}."
c = lc(32, include_mlp=False)
assert c["target_modules"] == att and c["lora_alpha"] == 64, "Without the MLP, target only the four attention modules."
s = sc(3, 1e-4, 1, 16)
want = {"output_dir": "out", "num_train_epochs": 3, "learning_rate": 1e-4, "per_device_train_batch_size": 1,
        "gradient_accumulation_steps": 16, "lr_scheduler_type": "cosine", "warmup_ratio": 0.05, "bf16": True}
assert s == want, f"make_sft_config(3, 1e-4, 1, 16) returned {s!r}, expected {want!r}."
