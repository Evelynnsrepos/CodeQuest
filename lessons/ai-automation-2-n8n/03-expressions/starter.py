import re


def render(text, item, nodes):
    return text


item = {"from": "anna@x.de", "sender": {"name": "Anna"}}
nodes = {"Read Email": {"subject": "Hi there"}}
print(render("{{ $json.sender.name }} <{{$json.from}}>: {{ $('Read Email').item.json.subject }}", item, nodes))
