FORMATS = [("FP16", 16), ("Q8", 8.5), ("Q4_K_M", 4.5)]


def model_gb(params_b, bits):
    # return params_b * bits / 8
    return 0.0


def best_fit(params_b, vram_gb, overhead=1.5):
    # for name, bits in FORMATS:
    #     needed = model_gb(params_b, bits) + overhead
    #     if needed <= vram_gb: return name
    # after the loop: return None
    return None


print(model_gb(8, 16), best_fit(8, 12), best_fit(70, 12))
