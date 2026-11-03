def gpt_params(layers, d, vocab):
    return 12 * layers * d ** 2 + vocab * d


def full_finetune_gb(params):
    return params * 16 / 1e9


def qlora_gb(params, trainable):
    return (params * 0.5 + trainable * 16) / 1e9


print(f"GPT-2 small (12 layers, d=768, vocab 50257): {gpt_params(12, 768, 50257) / 1e6:.0f}M parameters")
print(f"full fine-tune of 8B: {full_finetune_gb(8e9):.0f} GB + activations")
print(f"QLoRA of 8B with 40M trainable: {qlora_gb(8e9, 40e6):.1f} GB + activations")

full_8b_fits = False
qlora_8b_fits = True
