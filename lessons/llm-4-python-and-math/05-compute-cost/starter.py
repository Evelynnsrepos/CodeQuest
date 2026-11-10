def matmul_flops(m, k, n):
    # return 2 * m * k * n
    return 0


def training_flops(params, tokens):
    # return 6 * params * tokens
    return 0


def training_days(flops, tflops, utilization):
    # seconds = flops / (tflops * 1e12 * utilization)
    # return seconds / 86400
    return 0


llama = training_flops(8e9, 15e12)
print(f"Llama 3 8B: {llama:.1e} FLOPs")
print(f"  on one 26-TFLOPS GPU at 40%: {training_days(llama, 26, 0.4) / 365:,.0f} years")
toy = training_flops(10e6, 100e6)
print(f"Toy 10M model, 100M tokens: {toy:.1e} FLOPs")
print(f"  on the same GPU: {training_days(toy, 26, 0.4) * 24 * 60:.1f} minutes")
