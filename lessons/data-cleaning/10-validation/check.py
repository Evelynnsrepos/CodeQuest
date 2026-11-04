e, sv = ns.get("errors"), ns.get("split_valid")
assert e and sv, "Keep errors and split_valid."
S = {"email": {"type": str, "required": True, "check": lambda v: "@" in v},
     "age": {"type": int, "required": False, "check": lambda v: 0 <= v <= 120},
     "rating": {"type": int, "required": True}}
assert e({"email": "ada@x.de", "age": 36, "rating": 5}, S) == [], "A good row has no errors."
assert e({"email": "nope", "age": 150, "rating": "5"}, S) == ["email: invalid", "age: invalid", "rating: not int"], f"Got {e({'email': 'nope', 'age': 150, 'rating': '5'}, S)!r}."
assert e({"rating": 3}, S) == ["email: missing"], "Missing optional age is fine; missing required email is an error."
assert e({"email": 5, "rating": 1}, S) == ["email: not str"], "Wrong type: report it and skip that column's check."
good, bad = sv([{"email": "a@b", "rating": 1}, {"rating": 2}], S)
assert good == [{"email": "a@b", "rating": 1}] and bad == [({"rating": 2}, ["email: missing"])], f"Got {(good, bad)!r}."
