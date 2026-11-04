def quantize(ws, bits):
    return ws, 1


def dequantize(qs, scale):
    return qs


def max_error(ws, bits):
    return 0


ws = [0.5, -1.27, 0.03]
print(quantize(ws, 8), quantize(ws, 4), max_error(ws, 4), max_error(ws + [100], 8))
