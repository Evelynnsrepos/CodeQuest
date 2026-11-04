import math


class Value:
    """A number that remembers how it was computed, so it can compute gradients."""

    def __init__(self, data, _children=(), _op=""):
        self.data = data
        self.grad = 0.0
        self._backward = lambda: None
        self._prev = set(_children)
        self._op = _op

    def __repr__(self):
        return f"Value(data={self.data:.4f}, grad={self.grad:.4f})"

    def __add__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data + other.data, (self, other), "+")

        def _backward():
            pass  # how does out.grad flow into self.grad and other.grad?
        out._backward = _backward
        return out

    def __mul__(self, other):
        other = other if isinstance(other, Value) else Value(other)
        out = Value(self.data * other.data, (self, other), "*")

        def _backward():
            pass
        out._backward = _backward
        return out

    def backward(self):
        order, seen = [], set()
        # 1. visit every node so that each one comes after all of its children in order
        # 2. set this node's grad to 1.0
        # 3. call _backward on every node, in reversed order

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
