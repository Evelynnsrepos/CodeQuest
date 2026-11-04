V = ns.get("Value")
assert V, "Keep the class Value."
a, b, c = V(2.0), V(-3.0), V(10.0)
L = (a * b + c) * (a * b + c)
L.backward()
assert L.grad == 1.0, "backward() should set the output's grad to 1.0."
assert abs(a.grad - (-24)) < 1e-9 and abs(b.grad - 16) < 1e-9 and abs(c.grad - 8) < 1e-9, f"Got a.grad={a.grad}, b.grad={b.grad}, c.grad={c.grad}; expected −24, 16, 8."
x = V(3.0)
y = x * x + x
y.backward()
assert abs(x.grad - 7) < 1e-9, f"For y = x·x + x at x=3, dy/dx is 2·3 + 1 = 7, got {x.grad}. Use += so every use of x adds up."
p, q = V(5.0), V(7.0)
r = p + q
s = r * p
s.backward()
assert abs(p.grad - 17) < 1e-9 and abs(q.grad - 5) < 1e-9, f"For s = (p + q)·p at p=5, q=7: ds/dp = 17, ds/dq = 5. Got {p.grad}, {q.grad}. Check the topological order."
