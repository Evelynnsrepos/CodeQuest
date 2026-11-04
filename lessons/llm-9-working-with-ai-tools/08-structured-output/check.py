va, fv = ns.get("validate"), ns.get("first_valid")
assert va and fv, "Keep validate and first_valid."
s = {"type": "object", "required": ["spam"], "properties": {"spam": {"type": "boolean"}, "reason": {"type": "string"}, "label": {"enum": ["ham", "spam"]}, "score": {"type": "number"}, "n": {"type": "integer"}}}
assert va({"spam": True, "reason": "lottery"}, s) == [], "A valid object has no errors."
assert va({"spam": "yes"}, s), "spam must be a boolean."
assert va({"reason": "x"}, s), "spam is required."
assert va({"spam": False, "label": "maybe"}, s), "label must be in the enum."
assert va({"spam": True, "score": 0.7, "n": 3}, s) == [], "0.7 is a number, 3 an integer."
assert va({"spam": True, "score": True}, s), "A boolean is not a number."
assert va({"spam": True, "n": 2.5}, s), "2.5 is not an integer."
assert va([1], s), "Top-level type must be object."
assert fv(['Sure! {"spam": true}', '{"spam": "yes"}', '{"spam": true}'], s) == {"spam": True}, "Skip non-JSON and invalid replies."
assert fv(['x', 'y', 'z', '{"spam": true}'], s) is None, "Stop after max_tries."
