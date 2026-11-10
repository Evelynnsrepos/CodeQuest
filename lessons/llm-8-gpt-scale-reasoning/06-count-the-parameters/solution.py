def gpt2_params(vocab, ctx, d, layers):
    ln1 = 2 * d
    qkv = 3 * d * d + 3 * d
    proj = d * d + d
    ln2 = 2 * d
    up = 4 * d * d + 4 * d
    down = 4 * d * d + d
    per_layer = ln1 + qkv + proj + ln2 + up + down
    return vocab * d + ctx * d + layers * per_layer + 2 * d


def mlp_share(d):
    mlp = (4 * d * d + 4 * d) + (4 * d * d + d)
    layer = 12 * d * d + 13 * d
    return mlp / layer


print("GPT-2 small:", f"{gpt2_params(50257, 1024, 768, 12):,}")
print("GPT-2 XL:   ", f"{gpt2_params(50257, 1024, 1600, 48):,}")
print("MLP share of one layer at d=768:", round(mlp_share(768), 3))
