t = ns.get("ROLL_DICE")
assert isinstance(t, dict) and t.get("type") == "function", "ROLL_DICE needs \"type\": \"function\"."
f = t.get("function", {})
assert f.get("name") == "roll_dice", f"The name should be 'roll_dice', not {f.get('name')!r}."
assert len(f.get("description", "")) >= 10, "Give the tool a real description: it's all the model knows about it."
p = f.get("parameters", {})
assert p.get("type") == "object", "parameters must be a JSON Schema with \"type\": \"object\"."
props = p.get("properties", {})
for name in ("sides", "count"):
    assert name in props, f"properties is missing {name!r}."
    assert props[name].get("type") == "integer", f"{name!r} should have \"type\": \"integer\"."
    assert len(props[name].get("description", "")) >= 5, f"Describe the {name!r} parameter."
assert p.get("required") == ["sides"], f"required should be [\"sides\"], not {p.get('required')!r}."
