import re


def follow(value, path):
    for key in path.split("."):
        value = value[key]
    return value


def render(text, item, nodes):
    def fill(match):
        expr = match.group(1)
        m = re.match(r"\$\('(.+?)'\)\.item\.json\.(.+)", expr)
        if m:
            return str(follow(nodes[m.group(1)], m.group(2)))
        return str(follow(item, expr[len("$json."):]))
    return re.sub(r"\{\{\s*(.*?)\s*\}\}", fill, text)


item = {"from": "anna@x.de", "sender": {"name": "Anna"}}
nodes = {"Read Email": {"subject": "Hi there"}}
print(render("{{ $json.sender.name }} <{{$json.from}}>: {{ $('Read Email').item.json.subject }}", item, nodes))
