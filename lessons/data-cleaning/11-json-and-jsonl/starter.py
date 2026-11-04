import json


def flatten(d, prefix=""):
    return d


def read_jsonl(text):
    return [], []


print(flatten({"user": {"name": "Ada", "address": {"city": "Berlin"}}, "tags": ["a", "b"]}))
text = '{"prompt": "hi", "answer": "hello"}\n\n{broken\n[1, 2]\n{"prompt": "x", "answer": "y"}\n'
print(read_jsonl(text))
