import json


def make_lora_config(r, include_mlp=True):
    # targets = ["q_proj", "k_proj", "v_proj", "o_proj"]
    # if include_mlp:
    #     targets = targets + ["gate_proj", "up_proj", "down_proj"]
    # config = {}
    # config["r"] = r
    # config["lora_alpha"] = 2 * r
    # config["lora_dropout"] = 0.05
    # config["target_modules"] = targets
    # config["task_type"] = "CAUSAL_LM"
    # return config
    return {}


def make_sft_config(epochs, lr, per_device, accumulation):
    # config = {}
    # config["output_dir"] = "out"
    # config["num_train_epochs"] = epochs
    # config["learning_rate"] = lr
    # config["per_device_train_batch_size"] = per_device
    # config["gradient_accumulation_steps"] = accumulation
    # config["lr_scheduler_type"] = "cosine"
    # config["warmup_ratio"] = 0.05
    # config["bf16"] = True
    # return config
    return {}


print(json.dumps(make_lora_config(16), indent=2))
print(json.dumps(make_sft_config(2, 2e-4, 2, 8), indent=2))
