ls, sv, SPEC, REQUIRED = ns.get("load_settings"), ns.get("safe_view"), ns.get("SPEC"), ns.get("REQUIRED")
assert ls and sv and SPEC, "Keep load_settings, safe_view and SPEC."
s = ls({"OPENAI_API_KEY": "sk-secret", "TEMPERATURE": "0", "DEBUG": "Yes", "MAX_TOKENS": "64"})
assert s == {"MODEL": "llama3.2", "BASE_URL": "http://localhost:11434/v1", "TEMPERATURE": 0.0, "MAX_TOKENS": 64, "DEBUG": True, "OPENAI_API_KEY": "sk-secret"}, f"Got {s!r}."
assert type(s["TEMPERATURE"]) is float and type(s["MAX_TOKENS"]) is int, "Convert the types."
assert ls({"OPENAI_API_KEY": "x", "DEBUG": "nope"})["DEBUG"] is False, "Unknown bool text → False."
spec = {"B": (str, REQUIRED), "A": (int, REQUIRED), "C": (str, "c")}
try:
    ls({}, spec)
    raise AssertionError("Missing required settings must raise ValueError.")
except ValueError as e:
    assert str(e) == "missing settings: A, B", f"List all missing names, sorted: got {str(e)!r}."
v = sv({"OPENAI_API_KEY": "sk", "GH_TOKEN": "t", "DB_PASSWORD": "p", "MODEL": "m"})
assert v == {"OPENAI_API_KEY": "****", "GH_TOKEN": "****", "DB_PASSWORD": "****", "MODEL": "m"}, f"Got {v!r}."
