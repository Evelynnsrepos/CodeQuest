import json


def flatten(d, prefix=""):
    out = {}
    for k, v in d.items():
        name = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            out.update(flatten(v, name))
        else:
            out[name] = v
    return out


def read_jsonl(text):
    records, bad = [], []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        try:
            obj = json.loads(line)
        except json.JSONDecodeError:
            bad.append(n)
            continue
        if isinstance(obj, dict):
            records.append(obj)
        else:
            bad.append(n)
    return records, bad


print(flatten({"user": {"name": "Ada", "address": {"city": "Berlin"}}, "tags": ["a", "b"]}))
text = '{"prompt": "hi", "answer": "hello"}\n\n{broken\n[1, 2]\n{"prompt": "x", "answer": "y"}\n'
print(read_jsonl(text))
