def quantize(ws, bits):
    q_max = 2 ** (bits - 1) - 1
    scale = max(abs(w) for w in ws) / q_max
    return [round(w / scale) for w in ws], scale


def dequantize(qs, scale):
    return [q * scale for q in qs]


def max_error(ws, bits):
    qs, scale = quantize(ws, bits)
    return max(abs(w - h) for w, h in zip(ws, dequantize(qs, scale)))


ws = [0.5, -1.27, 0.03]
print(quantize(ws, 8), quantize(ws, 4), max_error(ws, 4), max_error(ws + [100], 8))
