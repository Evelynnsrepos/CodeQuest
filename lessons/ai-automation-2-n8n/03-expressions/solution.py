import re


def follow(value, path):
    for key in path.split("."):
        value = value[key]
    return value


def value_of(expr, item, nodes):
    if expr.startswith("$('"):
        end = expr.index("')")
        name = expr[3:end]
        path = expr[end + len("').item.json."):]
        return str(follow(nodes[name], path))
    return str(follow(item, expr[len("$json."):]))


# Given: you don't need to change this.
def render(text, item, nodes):
    def fill(match):
        return value_of(match.group(1), item, nodes)
    return re.sub(r"\{\{\s*(.*?)\s*\}\}", fill, text)


item = {"from": "anna@x.de", "sender": {"name": "Anna"}}
nodes = {"Read Email": {"subject": "Hi there"}}
print(render("{{ $json.sender.name }} <{{$json.from}}>: {{ $('Read Email').item.json.subject }}", item, nodes))
