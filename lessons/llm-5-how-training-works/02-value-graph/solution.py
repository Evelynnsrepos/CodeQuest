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
        if not isinstance(other, Value):  # lets you write v + 1
            other = Value(other)
        return Value(self.data + other.data, (self, other), "+")

    def __mul__(self, other):
        if not isinstance(other, Value):
            other = Value(other)
        return Value(self.data * other.data, (self, other), "*")

    def __radd__(self, other): return self + other
    def __rmul__(self, other): return self * other


a = Value(2.0)
b = Value(-3.0)
c = Value(10.0)
d = a * b + c
print(d)
print("made by:", d._op, "from", sorted(v.data for v in d._prev))
