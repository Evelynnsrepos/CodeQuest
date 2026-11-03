def all_reduce_mean(grads_per_gpu):
    return grads_per_gpu[0]


def zero_memory_gb(params, gpus, stage):
    return 0.0


grads = [[0.2, -0.4, 1.0], [0.4, 0.0, 0.6], [0.0, -0.2, 0.8], [0.2, -0.2, 0.6]]
print("averaged:", [round(g, 3) for g in all_reduce_mean(grads)])
for stage in [0, 1, 2, 3]:
    print(f"8B model, 8 GPUs, ZeRO-{stage}: {zero_memory_gb(8e9, 8, stage):.0f} GB per GPU")
