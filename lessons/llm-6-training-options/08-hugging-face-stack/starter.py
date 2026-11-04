import json


def make_lora_config(r, include_mlp=True):
    return {}


def make_sft_config(epochs, lr, per_device, accumulation):
    return {}


print(json.dumps(make_lora_config(16), indent=2))
print(json.dumps(make_sft_config(2, 2e-4, 2, 8), indent=2))
