f = ns.get("extract_json")
assert f, "Define a function called extract_json."
fence = "`" * 3
assert f('{"a": 1}') == {"a": 1}, "Plain JSON."
assert f(f'Sure!\n{fence}json\n{{"label": "work", "urgent": true}}\n{fence}\nHope that helps!') == {"label": "work", "urgent": True}, "Take the JSON out of a json fence."
assert f(f'{fence}\n{{"x": [1, 2]}}\n{fence}') == {"x": [1, 2]}, "A fence without 'json' works too."
assert f('The answer is {"label": "spam"} I think.') == {"label": "spam"}, "No fence: first { to last }."
assert f('Result: {"a": {"b": 2}} done') == {"a": {"b": 2}}, "Nested objects: go to the last }."
assert f("I can't decide.") is None, "No JSON at all: None."
assert f('{"label": work}') is None, "Broken JSON: None, don't crash."
assert f("} oops {") is None, "Braces in the wrong order: None."
