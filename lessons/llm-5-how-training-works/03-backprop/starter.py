import math


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
            # self.grad += out.grad
            # other.grad += out.grad
            pass
        out._backward = _backward
        return out

    def __mul__(self, other):
        if not isinstance(other, Value):
            other = Value(other)
        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            # self.grad += other.data * out.grad
            # other.grad += self.data * out.grad
            pass
        out._backward = _backward
        return out

    def backward(self):
        order, seen = [], set()
        # def visit(v):
        #     if v not in seen:
        #         seen.add(v)
        #         for child in v._prev:
        #             visit(child)
        #         order.append(v)
        # visit(self)
        # self.grad = 1.0
        # for v in reversed(order):
        #     v._backward()

    def __radd__(self, other): return self + other
    def __rmul__(self, other): return self * other


a = Value(2.0)
b = Value(-3.0)
c = Value(10.0)
e = a * b
d = e + c
L = d * d
L.backward()
for name, v in [("a", a), ("b", b), ("c", c), ("e", e), ("d", d), ("L", L)]:
    print(name, v)
