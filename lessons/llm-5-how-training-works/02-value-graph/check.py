V = ns.get("Value")
assert V, "Keep the class Value."
a, b = V(3.0), V(4.0)
s = a + b
assert isinstance(s, V), "a + b should return a new Value."
assert s.data == 7.0 and s._op == "+" and s._prev == {a, b}, f"a + b gave data={getattr(s, 'data', None)!r}, op={getattr(s, '_op', None)!r}. Children should be (self, other)."
p = a * b
assert isinstance(p, V) and p.data == 12.0 and p._op == "*" and p._prev == {a, b}, "a * b should give a Value with data 12, op '*' and children a and b."
q = a * 2 + 1
assert q.data == 7.0, f"a * 2 + 1 gave {q.data!r}, expected 7 (plain numbers get wrapped in Values)."
assert a.data == 3.0 and b.data == 4.0, "Don't change the inputs; return a new Value."
