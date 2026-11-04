f = ns.get("render")
assert f, "Define a function called render."
item = {"from": "anna@x.de", "n": 3, "sender": {"name": "Anna", "tags": {"vip": True}}}
nodes = {"Read Email": {"subject": "Hi"}, "AI Agent": {"output": {"label": "work"}}}
assert f("From {{ $json.from }}", item, nodes) == "From anna@x.de", "Replace $json.from."
assert f("{{$json.from}}", item, nodes) == "anna@x.de", "Spaces inside the braces are optional."
assert f("{{ $json.sender.name }} {{ $json.sender.tags.vip }}", item, nodes) == "Anna True", "Follow dotted paths, use str()."
assert f("x{{ $json.n }}y", item, nodes) == "x3y", "Numbers become text."
assert f("{{ $('Read Email').item.json.subject }}", item, nodes) == "Hi", "Read from an earlier node by name."
assert f("{{ $('AI Agent').item.json.output.label }}!", item, nodes) == "work!", "Paths work in the node form too."
assert f("no expressions", item, nodes) == "no expressions", "Text without {{ }} stays the same."
