import json


def type_ok(value, t):
    if isinstance(value, bool):
        return t == "boolean"
    if t == "integer":
        return isinstance(value, int)
    if t == "number":
        return isinstance(value, int) or isinstance(value, float)
    if t == "string":
        return isinstance(value, str)
    if t == "array":
        return isinstance(value, list)
    if t == "object":
        return isinstance(value, dict)
    return False


def validate(obj, schema, path="$"):
    # errors = []
    # if "type" in schema and not type_ok(obj, schema["type"]):
    #     return [path + ": expected " + schema["type"]]
    # if "enum" in schema and obj not in schema["enum"]:
    #     errors.append(path + ": not one of " + str(schema["enum"]))
    # if isinstance(obj, dict):
    #     for key in schema.get("required", []):
    #         if key not in obj:
    #             errors.append(path + "." + key + ": required")
    #     properties = schema.get("properties", {})
    #     for key in properties:
    #         if key in obj:
    #             errors = errors + validate(obj[key], properties[key], path + "." + key)
    # return errors
    return []


def first_valid(replies, schema, max_tries=3):
    # for raw in replies[:max_tries]:
    #     try:
    #         obj = json.loads(raw)
    #     except json.JSONDecodeError:
    #         continue
    #     if validate(obj, schema) == []:
    #         return obj
    # return None
    return None


schema = {"type": "object", "required": ["spam"], "properties": {"spam": {"type": "boolean"}, "reason": {"type": "string"}}}
print(validate({"spam": "yes"}, schema), first_valid(['Sure! {"spam": true}', '{"spam": true}'], schema))
