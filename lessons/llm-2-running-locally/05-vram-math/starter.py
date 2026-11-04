def kv_cache_gb(layers, kv_heads, head_dim, context, bytes_per_value):
    return 0


def total_vram_gb(weights_gb, kv_gb):
    return 0


def max_context(weights_gb, layers, kv_heads, head_dim, budget_gb):
    context = 0
    return context


# Llama 3.1 8B at Q4_K_M
print(round(kv_cache_gb(32, 8, 128, 8192, 2), 2), "GB KV cache at 8k context")
print(round(total_vram_gb(4.9, kv_cache_gb(32, 8, 128, 8192, 2)), 2), "GB in total")
print(max_context(4.9, 32, 8, 128, 11.0), "tokens max with 11 GB usable")
