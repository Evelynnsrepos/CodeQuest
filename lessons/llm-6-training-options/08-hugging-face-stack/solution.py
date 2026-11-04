import json


def make_lora_config(r, include_mlp=True):
    targets = ["q_proj", "k_proj", "v_proj", "o_proj"]
    if include_mlp:
        targets += ["gate_proj", "up_proj", "down_proj"]
    return {"r": r, "lora_alpha": 2 * r, "lora_dropout": 0.05,
            "target_modules": targets, "task_type": "CAUSAL_LM"}


def make_sft_config(epochs, lr, per_device, accumulation):
    return {"output_dir": "out", "num_train_epochs": epochs, "learning_rate": lr,
            "per_device_train_batch_size": per_device, "gradient_accumulation_steps": accumulation,
            "lr_scheduler_type": "cosine", "warmup_ratio": 0.05, "bf16": True}


print(json.dumps(make_lora_config(16), indent=2))
print(json.dumps(make_sft_config(2, 2e-4, 2, 8), indent=2))
