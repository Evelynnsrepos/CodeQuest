class Linear:
    def __init__(self, weights, bias):
        pass

    def __call__(self, x):
        return []

    def num_params(self):
        return 0


class Sequential:
    def __init__(self, layers):
        pass

    def __call__(self, x):
        return x


layer1 = Linear([[1, 0], [0, 1], [1, 1]], [0, 0, 1])   # 2 inputs → 3 outputs
layer2 = Linear([[1, -1, 2]], [0.5])                   # 3 inputs → 1 output
model = Sequential([layer1, layer2])
print(layer1([2, 3]))
print(model([2, 3]))
print(layer1.num_params() + layer2.num_params(), "parameters")
