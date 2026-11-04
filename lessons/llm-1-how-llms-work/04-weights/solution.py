def neuron(inputs, weights, bias):
    total = 0
    for x, w in zip(inputs, weights):
        total += x * w
    return total + bias


def model_size_gb(params_billion, bits):
    return params_billion * bits / 8


print(neuron([2.0, 3.0], [0.5, -1.0], 0.25))
print(model_size_gb(8, 16), "GB for an 8B model in FP16")
print(model_size_gb(8, 4.8), "GB for an 8B model in Q4_K_M")

fp16_8b_fits_in_12gb = False  # True or False
