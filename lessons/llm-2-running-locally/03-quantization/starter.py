def quantize(block):
    # biggest = 0
    # for w in block:
    #     if abs(w) > biggest:
    #         biggest = abs(w)
    scale = 1.0
    # if biggest > 0:
    #     scale = biggest / 7
    qs = []
    # for w in block:
    #     q = round(w / scale)
    #     q = max(-8, min(7, q))
    #     qs.append(q)
    return scale, qs


def dequantize(scale, qs):
    # restored = []
    # for q in qs:
    #     restored.append(q * scale)
    # return restored
    return []


def max_error(block):
    """Given: the biggest difference between a weight and its restored value."""
    scale, qs = quantize(block)
    restored = dequantize(scale, qs)
    if len(restored) != len(block):
        return None
    worst = 0
    for i in range(len(block)):
        if abs(block[i] - restored[i]) > worst:
            worst = abs(block[i] - restored[i])
    return worst


normal = [0.12, -0.40, 0.05, 0.33, -0.21, 0.02, 0.18, -0.09]
outlier = [0.12, -0.40, 0.05, 0.33, -0.21, 0.02, 0.18, 6.50]
print("quantized:", quantize(normal)[1])
print("max error, normal block: ", max_error(normal))
print("quantized:", quantize(outlier)[1])
print("max error, outlier block:", max_error(outlier))

outlier_hurts = None  # True or False
