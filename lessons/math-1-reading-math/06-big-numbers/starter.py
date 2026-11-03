def human(n):
    return str(n)


def model_gb(params, bytes_per_param):
    return 0.0


print(human(8e9), human(1.5e13), human(124_439_808), human(3500), human(42))
print(model_gb(8e9, 2), "GB in FP16")
