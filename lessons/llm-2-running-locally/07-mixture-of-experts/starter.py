def size_gb(params_billion, bpw):
    # return params_billion * bpw / 8
    return 0


def speed_from_ram(active_billion, bpw, ram_bw):
    # return ram_bw / size_gb(active_billion, bpw)
    return 0


print("Qwen3-30B-A3B at Q4_K_M:", round(size_gb(30.5, 4.8), 1), "GB to store")
print("  from RAM:", round(speed_from_ram(3.3, 4.8, 51), 1), "tok/s")
print("dense 14B at Q4_K_M:    ", round(size_gb(14, 4.8), 1), "GB to store")
print("  from RAM:", round(speed_from_ram(14, 4.8, 51), 1), "tok/s")

faster = ""  # "dense" or "moe"
