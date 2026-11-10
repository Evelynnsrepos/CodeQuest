class Linear:
    def __init__(self, weights, bias):
        self.weights = weights
        self.bias = bias

    def __call__(self, x):
        out = []
        for j in range(len(self.weights)):
            row = self.weights[j]
            total = 0
            for i in range(len(x)):
                total = total + row[i] * x[i]
            out.append(total + self.bias[j])
        return out

    def num_params(self):
        count = 0
        for row in self.weights:
            count = count + len(row)
        return count + len(self.bias)


class Sequential:
    def __init__(self, layers):
        self.layers = layers

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x


layer1 = Linear([[1, 0], [0, 1], [1, 1]], [0, 0, 1])   # 2 inputs → 3 outputs
layer2 = Linear([[1, -1, 2]], [0.5])                   # 3 inputs → 1 output
model = Sequential([layer1, layer2])
print(layer1([2, 3]))
print(model([2, 3]))
print(layer1.num_params() + layer2.num_params(), "parameters")
