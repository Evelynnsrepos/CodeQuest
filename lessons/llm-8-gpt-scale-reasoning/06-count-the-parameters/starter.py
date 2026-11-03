def gpt2_params(vocab, ctx, d, layers):
    return 0


def mlp_share(d):
    return 0.0


print("GPT-2 small:", f"{gpt2_params(50257, 1024, 768, 12):,}")
print("GPT-2 XL:   ", f"{gpt2_params(50257, 1024, 1600, 48):,}")
print("MLP share of one layer at d=768:", round(mlp_share(768), 3))
