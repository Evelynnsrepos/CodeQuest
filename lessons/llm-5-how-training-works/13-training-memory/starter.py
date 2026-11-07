def gpt_params(layers, d, vocab):
    # return 12 * layers * d ** 2 + vocab * d
    return 0


def full_finetune_gb(params):
    # return params * 16 / 1e9
    return 0


def qlora_gb(params, trainable):
    # return (params * 0.5 + trainable * 16) / 1e9
    return 0


print(f"GPT-2 small (12 layers, d=768, vocab 50257): {gpt_params(12, 768, 50257) / 1e6:.0f}M parameters")
print(f"full fine-tune of 8B: {full_finetune_gb(8e9):.0f} GB + activations")
print(f"QLoRA of 8B with 40M trainable: {qlora_gb(8e9, 40e6):.1f} GB + activations")

full_8b_fits = None  # True or False: does 128 GB + 3 GB fit in 12 GB?
qlora_8b_fits = None  # True or False: does 4.6 GB + 3 GB fit in 12 GB?
