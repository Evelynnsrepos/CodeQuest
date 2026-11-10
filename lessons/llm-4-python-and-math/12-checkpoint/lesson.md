---
title: Checkpoint: a script that asks LM Studio
minutes: 50
xp: 70
hint: Build the dictionary first: payload = {"model": model, "messages": [...], "temperature": 0.2, "max_tokens": 300}
hint: messages is a list of two dictionaries: {"role": "system", "content": "Answer briefly."} and {"role": "user", "content": question}
hint: req = urllib.request.Request(base_url + "/chat/completions", data=json.dumps(payload).encode("utf-8"), headers={"Content-Type": "application/json"})
hint: with urllib.request.urlopen(req, timeout=120) as response: and inside it data = json.loads(response.read())
hint: Last line: return data["choices"][0]["message"]["content"]
---
# Checkpoint

⏱️ About 50 minutes

The Module 4 checkpoint, from your plan: *write a Python script that calls your LM Studio server's API and prints the model's answer.* Standard library only, no `pip install`.

CodeQuest runs your code in the browser, which can't reach LM Studio, so the check swaps `urllib.request.urlopen` for a fake server and inspects exactly what your code sends. Then you run the same file for real.

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `payload = {"model": model, ...}` | | a dictionary: the request you send. Lists and dictionaries can sit inside each other. |
| `json.dumps(payload)` | "json dumps" | the dictionary as JSON **text** |
| `.encode("utf-8")` | | the text as **bytes**, what the network sends |
| `urllib.request.Request(url, data=..., headers=...)` | | packs address, body and headers into one request. Giving `data=` makes it a POST. |
| `with urllib.request.urlopen(req, timeout=120) as response:` | | sends it, waits up to 120 seconds, and calls the answer `response`. `with` closes the connection afterwards. |
| `json.loads(response.read())` | "json loads" | the answer's JSON text back into a dictionary |
| `data["choices"][0]["message"]["content"]` | | go in step by step: the `choices` list → its first item → its `message` → its `content` |
| `def ask(question, model="local-model", ...)` | | inputs with **defaults**, used when the caller leaves them out |

Call it as `urllib.request.urlopen(...)` exactly like that (the check replaces that function).

### 👀 Worked example: digging out the answer

The server answers with JSON like this:

```python
data = {"choices": [{"index": 0, "message": {"role": "assistant", "content": "Hi!"}}]}
```

1. `data["choices"]` → the list `[{"index": 0, "message": {...}}]`
2. `[0]` → its first item `{"index": 0, "message": {...}}`
3. `["message"]` → `{"role": "assistant", "content": "Hi!"}`
4. `["content"]` → `"Hi!"`

## 🎯 Your quest

Write `ask(question, model, base_url)`. Replace `return ""` with these lines (inside the brackets, the indent is only for reading):

1. `    payload = {`
2. `        "model": model,`
3. `        "messages": [`
4. `            {"role": "system", "content": "Answer briefly."},`
5. `            {"role": "user", "content": question},`
6. `        ],`
7. `        "temperature": 0.2,`
8. `        "max_tokens": 300,`
9. `    }`
10. `    req = urllib.request.Request(`
11. `        base_url + "/chat/completions",`
12. `        data=json.dumps(payload).encode("utf-8"),`
13. `        headers={"Content-Type": "application/json"},`
14. `    )`
15. `    with urllib.request.urlopen(req, timeout=120) as response:`
16. `        data = json.loads(response.read())`
17. `    return data["choices"][0]["message"]["content"]`

Leave `RUN_FOR_REAL = False` in CodeQuest.

## On your machine (the real checkpoint)

1. In LM Studio, load a model and start the server (*Developer* tab, or `lms server start`). `lms ps` shows the loaded model's name; put it in `model=`.
2. Copy your code into `~/llm-course/ask.py` and set `RUN_FOR_REAL = True`.
3. Run it: `python3 ask.py` (on NixOS without a global Python: `nix shell nixpkgs#python3 -c python3 ask.py`).
4. Extend it yourself: take the question from the command line (`sys.argv`), print the token usage, then turn it into a chat loop that keeps the history (and watch the prompt tokens grow, LLMs 1 lesson 13).

## What's next

LLMs 5: how training actually works. You'll build an automatic-differentiation engine, a neural network and a character-level language model from scratch.
