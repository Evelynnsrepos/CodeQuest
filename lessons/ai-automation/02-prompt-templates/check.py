f = ns.get("fill")
assert f, "Define a function called fill."
got = f("Hi {name}, you have {n} tasks.", {"name": "Eve", "n": 3})
assert got == "Hi Eve, you have 3 tasks.", f"Got {got!r}."
assert f("No blanks here.", {}) == "No blanks here.", "A template without blanks comes back unchanged."
try:
    f("From {date}: {note}", {"note": "x"})
except ValueError as e:
    assert str(e) == "missing field: date", f"The error should say 'missing field: date', not {str(e)!r}."
except KeyError:
    raise AssertionError("Catch the KeyError and raise a ValueError instead.")
else:
    raise AssertionError("A missing field should raise ValueError.")
