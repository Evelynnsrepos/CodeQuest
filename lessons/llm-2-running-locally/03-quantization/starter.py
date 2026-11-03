def quantize(block):
    scale = 1.0
    qs = []
    return scale, qs


def dequantize(scale, qs):
    return []


def max_error(block):
    scale, qs = quantize(block)
    restored = dequantize(scale, qs)
    if len(restored) != len(block):
        return None
    return max(abs(a - b) for a, b in zip(block, restored))


normal = [0.12, -0.40, 0.05, 0.33, -0.21, 0.02, 0.18, -0.09]
outlier = [0.12, -0.40, 0.05, 0.33, -0.21, 0.02, 0.18, 6.50]
print("quantized:", quantize(normal)[1])
print("max error, normal block: ", max_error(normal))
print("quantized:", quantize(outlier)[1])
print("max error, outlier block:", max_error(outlier))

outlier_hurts = None  # True or False
