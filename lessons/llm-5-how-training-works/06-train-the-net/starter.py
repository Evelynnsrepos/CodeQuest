import math
import random


# ---- your micrograd from lessons 2–4 ----
def do_nothing():
    """The starting _backward: a leaf value has no children to pass a gradient to."""
    pass


class Value:
    """A number that remembers how it was computed, so it can compute gradients."""

    def __init__(self, data, _children=(), _op=""):
        self.data = data
        self.grad = 0.0
        self._backward = do_nothing
        self._prev = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data={self.data:.4f}, grad={self.grad:.4f})"

    def __add__(self, other):
        if not isinstance(other, Value):
            other = Value(other)
        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            self.grad += out.grad
            other.grad += out.grad
        out._backward = _backward
        return out

    def __mul__(self, other):
        if not isinstance(other, Value):
            other = Value(other)
        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            self.grad += other.data * out.grad
            other.grad += self.data * out.grad
        out._backward = _backward
        return out

    def __pow__(self, k):
        out = Value(self.data ** k, (self,), f"**{k}")

        def _backward():
            self.grad += k * self.data ** (k - 1) * out.grad
        out._backward = _backward
        return out

    def tanh(self):
        t = math.tanh(self.data)
        out = Value(t, (self,), "tanh")

        def _backward():
            self.grad += (1 - t ** 2) * out.grad
        out._backward = _backward
        return out

    def relu(self):
        out = Value(max(0.0, self.data), (self,), "relu")

        def _backward():
            if self.data > 0:
                self.grad += out.grad
        out._backward = _backward
        return out

    def backward(self):
        order, seen = [], set()

        def visit(v):
            if v not in seen:
                seen.add(v)
                for child in v._prev:
                    visit(child)
                order.append(v)
        visit(self)
        self.grad = 1.0
        for v in reversed(order):
            v._backward()

    def __neg__(self): return self * -1
    def __sub__(self, other): return self + (-other)
    def __radd__(self, other): return self + other
    def __rsub__(self, other): return (-self) + other
    def __rmul__(self, other): return self * other
    def __truediv__(self, other): return self * other ** -1


# ---- neural network ----
class Neuron:
    def __init__(self, n_inputs, activation=True):
        self.w = []
        for i in range(n_inputs):
            self.w.append(Value(random.uniform(-1, 1)))
        self.b = Value(0.0)
        self.activation = activation

    def __call__(self, x):
        total = self.b
        for i in range(len(self.w)):
            total = total + self.w[i] * x[i]
        if self.activation:
            return total.tanh()
        return total

    def parameters(self):
        return self.w + [self.b]


class Layer:
    def __init__(self, n_inputs, n_outputs, activation=True):
        self.neurons = []
        for i in range(n_outputs):
            self.neurons.append(Neuron(n_inputs, activation))

    def __call__(self, x):
        outputs = []
        for n in self.neurons:
            outputs.append(n(x))
        return outputs

    def parameters(self):
        params = []
        for n in self.neurons:
            params = params + n.parameters()
        return params


class MLP:
    def __init__(self, n_inputs, layer_sizes):
        sizes = [n_inputs] + layer_sizes
        self.layers = []
        for i in range(len(layer_sizes)):
            is_last = i == len(layer_sizes) - 1
            self.layers.append(Layer(sizes[i], sizes[i + 1], activation=not is_last))

    def __call__(self, x):
        for layer in self.layers:
            x = layer(x)
        return x

    def parameters(self):
        params = []
        for layer in self.layers:
            params = params + layer.parameters()
        return params


def train(model, xs, ys, learning_rate, steps):
    for step in range(steps):
        loss = Value(0.0)
        # predictions = []
        # for x in xs:
        #     predictions.append(model(x)[0])
        # loss = Value(0.0)
        # for i in range(len(ys)):
        #     loss = loss + (predictions[i] - ys[i]) ** 2
        # for p in model.parameters():
        #     p.grad = 0.0
        # loss.backward()
        # for p in model.parameters():
        #     p.data = p.data - learning_rate * p.grad
        if step % 10 == 0:
            print(f"step {step:3}: loss {loss.data:.4f}")
    return loss.data


random.seed(1)
xs = [[2.0, 3.0, -1.0], [3.0, -1.0, 0.5], [0.5, 1.0, 1.0], [1.0, 1.0, -1.0]]
ys = [1.0, -1.0, -1.0, 1.0]
model = MLP(3, [4, 4, 1])
final = train(model, xs, ys, 0.01, 60)
print("final loss:", round(final, 4))
print("predictions:", [round(model(x)[0].data, 2) for x in xs], "targets:", ys)
