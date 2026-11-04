import json
import urllib.request

RUN_FOR_REAL = False


def ask(question, model="local-model", base_url="http://localhost:1234/v1"):
    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "Answer briefly."},
            {"role": "user", "content": question},
        ],
        "temperature": 0.2,
        "max_tokens": 300,
    }
    req = urllib.request.Request(
        base_url + "/chat/completions",
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
    )
    with urllib.request.urlopen(req, timeout=120) as response:
        data = json.loads(response.read())
    return data["choices"][0]["message"]["content"]


if RUN_FOR_REAL:
    print(ask("In one sentence: what is a KV cache?"))
