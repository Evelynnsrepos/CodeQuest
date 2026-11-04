BPW = {"F16": 16.0, "Q8_0": 8.5, "Q6_K": 6.6, "Q5_K_M": 5.7, "Q4_K_M": 4.8,
       "IQ4_XS": 4.3, "Q3_K_M": 3.9, "Q2_K": 2.9}


def file_size_gb(params_billion, quant):
    return 0


def best_quant(params_billion, budget_gb):
    return None


for size in [4, 8, 14, 24, 32]:
    q = best_quant(size, 10)
    print(f"{size}B: {q}", f"({file_size_gb(size, q):.1f} GB)" if q else "")
