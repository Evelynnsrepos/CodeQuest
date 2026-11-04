import math


def epsilon(man_bits):
    return 0


def max_value(exp_bits, man_bits):
    return 0


def round_to_bits(x, man_bits):
    return x


def bytes_for(n_params, fmt):
    return 0


print(epsilon(7), max_value(5, 10), round_to_bits(1.001, 7), round_to_bits(0.1, 10), bytes_for(7e9, "bf16"))
