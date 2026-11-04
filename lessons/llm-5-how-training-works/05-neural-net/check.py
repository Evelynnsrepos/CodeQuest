V, N, Lr, M = ns.get("Value"), ns.get("Neuron"), ns.get("Layer"), ns.get("MLP")
assert V and N and Lr and M, "Keep Value, Neuron, Layer and MLP."
n = N(2)
n.w[0].data, n.w[1].data, n.b.data = 0.5, -1.0, 0.25
out = n([2.0, 1.0])
assert isinstance(out, V), "Neuron(x) should return a Value."
import math
assert abs(out.data - math.tanh(0.25)) < 1e-9, f"Neuron with w=[0.5, −1], b=0.25 on [2, 1] gave {out.data!r}, expected tanh(1 − 1 + 0.25) ≈ {math.tanh(0.25):.4f}."
lin = N(2, activation=False)
lin.w[0].data, lin.w[1].data, lin.b.data = 2.0, 3.0, 1.0
assert abs(lin([1.0, 1.0]).data - 6.0) < 1e-9, "A neuron with activation=False should return the plain weighted sum plus bias."
assert len(n.parameters()) == 3 and all(isinstance(p, V) for p in n.parameters()), "Neuron.parameters() should return its 2 weights and its bias."
layer = Lr(3, 5)
assert len(layer([1.0, 2.0, 3.0])) == 5, "A Layer with 5 neurons should return 5 outputs."
assert len(layer.parameters()) == 20, f"Layer(3, 5).parameters() has {len(layer.parameters())} entries, expected 3·5 + 5 = 20."
m = M(3, [4, 4, 1])
assert len(m.parameters()) == 41, f"MLP(3, [4, 4, 1]) has {len(m.parameters())} parameters, expected 16 + 20 + 5 = 41."
y = m([1.0, -1.0, 0.5])
assert isinstance(y, list) and len(y) == 1 and isinstance(y[0], V), "MLP(x) should return the last layer's list of outputs."
y[0].backward()
assert any(p.grad != 0 for p in m.parameters()), "After backward(), the MLP's parameters should have gradients. Build the outputs from the Values."
