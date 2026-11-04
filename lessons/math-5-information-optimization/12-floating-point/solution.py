import math


def epsilon(man_bits):
    return 2.0 ** -man_bits


def max_value(exp_bits, man_bits):
    bias = 2 ** (exp_bits - 1) - 1
    return (2 - 2.0 ** -man_bits) * 2.0 ** bias


def round_to_bits(x, man_bits):
    if x == 0:
        return 0.0
    m, e = math.frexp(x)
    scale = 2 ** (man_bits + 1)
    return math.ldexp(round(m * scale) / scale, e)


def bytes_for(n_params, fmt):
    return n_params * {"fp32": 4, "bf16": 2, "fp16": 2, "fp8": 1}[fmt]


print(epsilon(7), max_value(5, 10), round_to_bits(1.001, 7), round_to_bits(0.1, 10), bytes_for(7e9, "bf16"))
