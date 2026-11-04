import json

TYPES = {"object": dict, "string": str, "array": list, "boolean": bool}


def type_ok(value, t):
    if t in ("number", "integer"):
        if isinstance(value, bool):
            return False
        return isinstance(value, int) if t == "integer" else isinstance(value, (int, float))
    return isinstance(value, TYPES[t])


def validate(obj, schema, path="$"):
    errors = []
    if "type" in schema and not type_ok(obj, schema["type"]):
        return [f"{path}: expected {schema['type']}"]
    if "enum" in schema and obj not in schema["enum"]:
        errors.append(f"{path}: not one of {schema['enum']}")
    if isinstance(obj, dict):
        for key in schema.get("required", []):
            if key not in obj:
                errors.append(f"{path}.{key}: required")
        for key, sub in schema.get("properties", {}).items():
            if key in obj:
                errors += validate(obj[key], sub, f"{path}.{key}")
    return errors


def first_valid(replies, schema, max_tries=3):
    for raw in replies[:max_tries]:
        try:
            obj = json.loads(raw)
        except json.JSONDecodeError:
            continue
        if not validate(obj, schema):
            return obj
    return None


schema = {"type": "object", "required": ["spam"], "properties": {"spam": {"type": "boolean"}, "reason": {"type": "string"}}}
print(validate({"spam": "yes"}, schema), first_valid(['Sure! {"spam": true}', '{"spam": true}'], schema))
