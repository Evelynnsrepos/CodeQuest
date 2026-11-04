---
title: Checkpoint: a script that asks LM Studio
xp: 70
---
# Checkpoint

The Module 4 checkpoint, from your plan: *write a Python script that calls your LM Studio server's API and prints the model's answer.* Standard library only, no `pip install`.

CodeQuest runs your code in the browser, which can't reach LM Studio, so the check swaps `urllib.request.urlopen` for a fake server and inspects exactly what your code sends. Then you run the same file for real.

## Python you need

```python
import json
import urllib.request

body = json.dumps({"some": "data"}).encode("utf-8")      # bytes to send
req = urllib.request.Request(url, data=body, headers={"Content-Type": "application/json"})
with urllib.request.urlopen(req, timeout=120) as response:   # giving data makes it a POST
    data = json.loads(response.read())
```

Call it as `urllib.request.urlopen(...)` exactly like that (the check replaces that function).

## Your quest

Write `ask(question, model="local-model", base_url="http://localhost:1234/v1")`:

1. Build a chat request (LLMs 2, lesson 10) with a system message `"Answer briefly."`, the user's `question`, `"temperature": 0.2` and `"max_tokens": 300`.
2. POST it as JSON to `base_url + "/chat/completions"`.
3. Return the assistant's message content.

Leave `RUN_FOR_REAL = False` in CodeQuest.

## On your machine (the real checkpoint)

1. In LM Studio, load a model and start the server (*Developer* tab, or `lms server start`). `lms ps` shows the loaded model's name; put it in `model=`.
2. Copy your code into `~/llm-course/ask.py` and set `RUN_FOR_REAL = True`.
3. Run it: `python3 ask.py` (on NixOS without a global Python: `nix shell nixpkgs#python3 -c python3 ask.py`).
4. Extend it yourself: take the question from the command line (`sys.argv`), print the token usage, then turn it into a chat loop that keeps the history (and watch the prompt tokens grow, LLMs 1 lesson 13).

## What's next

LLMs 5: how training actually works. You'll build an automatic-differentiation engine, a neural network and a character-level language model from scratch.
