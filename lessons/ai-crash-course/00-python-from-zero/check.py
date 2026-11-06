d, g = ns.get("double"), ns.get("greet")
assert d and g, "Keep the two lines that start with def double and def greet."
assert d(21) == 42 and d(5) == 10 and d(0) == 0, f"double(5) should give back 10, yours gave back {d(5)!r}. Use return x * 2."
assert g("Ada") == "Hello, Ada", f"greet('Ada') should give back 'Hello, Ada', yours gave back {g('Ada')!r}. Mind the comma and the space."
assert g("Evelynn") == "Hello, Evelynn", "Use the name you were given (the box name), not a fixed name."
