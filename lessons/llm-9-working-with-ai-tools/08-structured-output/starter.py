import json


def validate(obj, schema):
    return []


def first_valid(replies, schema, max_tries=3):
    return None


schema = {"type": "object", "required": ["spam"], "properties": {"spam": {"type": "boolean"}, "reason": {"type": "string"}}}
print(validate({"spam": "yes"}, schema), first_valid(['Sure! {"spam": true}', '{"spam": true}'], schema))
