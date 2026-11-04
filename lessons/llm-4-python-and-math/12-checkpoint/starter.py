import json
import urllib.request

RUN_FOR_REAL = False


def ask(question, model="local-model", base_url="http://localhost:1234/v1"):
    return ""


if RUN_FOR_REAL:
    print(ask("In one sentence: what is a KV cache?"))
