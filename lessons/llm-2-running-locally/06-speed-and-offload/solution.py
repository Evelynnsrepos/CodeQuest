def tokens_per_second(gpu_gb, cpu_gb, gpu_bw, cpu_bw):
    seconds = gpu_gb / gpu_bw + cpu_gb / cpu_bw
    return 1 / seconds


def layers_on_gpu(model_gb, layers, vram_free_gb):
    per_layer = model_gb / layers
    fit = int(vram_free_gb / per_layer)
    if fit > layers:
        fit = layers
    return fit


print("8B Q4 fully on GPU:", round(tokens_per_second(4.9, 0, 384, 51)), "tok/s")
print("24B Q4 (14.3 GB):", layers_on_gpu(14.3, 40, 10.0), "of 40 layers fit in 10 GB")
gpu_part = 14.3 * layers_on_gpu(14.3, 40, 10.0) / 40
print("24B Q4 offloaded:", round(tokens_per_second(gpu_part, 14.3 - gpu_part, 384, 51), 1), "tok/s")
