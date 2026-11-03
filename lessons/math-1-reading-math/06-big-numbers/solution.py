def human(n):
    for size, suffix in [(1e12, "T"), (1e9, "B"), (1e6, "M"), (1e3, "K")]:
        if n >= size:
            return f"{n / size:.1f}{suffix}"
    return str(n)


def model_gb(params, bytes_per_param):
    return params * bytes_per_param / 1e9


print(human(8e9), human(1.5e13), human(124_439_808), human(3500), human(42))
print(model_gb(8e9, 2), "GB in FP16")
