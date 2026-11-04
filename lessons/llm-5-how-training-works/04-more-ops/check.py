import math
V = ns.get("Value")
assert V, "Keep the class Value."
def numeric(f, x, h=1e-6):
    return (f(V(x + h)).data - f(V(x - h)).data) / (2 * h)
cases = [("x ** 3", lambda v: v ** 3, 1.7), ("x ** -1", lambda v: v ** -1, 2.0), ("tanh(x)", lambda v: v.tanh(), 0.3),
         ("tanh(2x)", lambda v: (v * 2).tanh(), -0.4), ("relu(x) at 1.2", lambda v: v.relu(), 1.2),
         ("relu(x) at -0.7", lambda v: v.relu(), -0.7), ("x / (1 + x²)", lambda v: v / (1 + v ** 2), 0.8)]
for name, f, x0 in cases:
    x = V(x0)
    y = f(x)
    y.backward()
    want = numeric(f, x0)
    assert abs(x.grad - want) < 1e-5, f"d/dx of {name} at x={x0}: autograd says {x.grad:.6f}, numerically it's {want:.6f}."
