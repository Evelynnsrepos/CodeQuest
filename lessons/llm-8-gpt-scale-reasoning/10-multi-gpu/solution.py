def all_reduce_mean(grads_per_gpu):
    n = len(grads_per_gpu)
    return [sum(col) / n for col in zip(*grads_per_gpu)]


def zero_memory_gb(params, gpus, stage):
    per_param = {0: 16, 1: 4 + 12 / gpus, 2: 2 + 14 / gpus, 3: 16 / gpus}[stage]
    return params * per_param / 1e9


grads = [[0.2, -0.4, 1.0], [0.4, 0.0, 0.6], [0.0, -0.2, 0.8], [0.2, -0.2, 0.6]]
print("averaged:", [round(g, 3) for g in all_reduce_mean(grads)])
for stage in [0, 1, 2, 3]:
    print(f"8B model, 8 GPUs, ZeRO-{stage}: {zero_memory_gb(8e9, 8, stage):.0f} GB per GPU")
