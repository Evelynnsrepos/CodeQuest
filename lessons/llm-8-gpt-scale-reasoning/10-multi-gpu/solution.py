def all_reduce_mean(grads_per_gpu):
    n = len(grads_per_gpu)
    out = []
    for i in range(len(grads_per_gpu[0])):
        total = 0
        for g in grads_per_gpu:
            total = total + g[i]
        out.append(total / n)
    return out


def zero_memory_gb(params, gpus, stage):
    if stage == 0:
        per_param = 16
    elif stage == 1:
        per_param = 4 + 12 / gpus
    elif stage == 2:
        per_param = 2 + 14 / gpus
    else:
        per_param = 16 / gpus
    return params * per_param / 1e9


grads = [[0.2, -0.4, 1.0], [0.4, 0.0, 0.6], [0.0, -0.2, 0.8], [0.2, -0.2, 0.6]]
print("averaged:", [round(g, 3) for g in all_reduce_mean(grads)])
for stage in [0, 1, 2, 3]:
    print(f"8B model, 8 GPUs, ZeRO-{stage}: {zero_memory_gb(8e9, 8, stage):.0f} GB per GPU")
