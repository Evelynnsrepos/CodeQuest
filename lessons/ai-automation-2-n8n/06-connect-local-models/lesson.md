---
title: Connect LM Studio and Ollama
minutes: 35
xp: 30
hint: Start: url = cfg["base_url"].rstrip("/") and problems = []
hint: Rules 1 and 2 are one if/elif: if url.endswith("/chat/completions"): ... elif url.endswith("/v1") == False: ...
hint: Rule 3: if cfg["n8n_in_docker"] and ("localhost" in url or "127.0.0.1" in url):
hint: Rule 4: if cfg["use_responses_api"]: and rule 5: if cfg["model"] == "": each followed by problems.append(...). At the end: return problems
---
# Fix the five classic setup mistakes

⏱️ About 35 minutes · one function, a list of checks

> **Warm-up:** n8n says "Bad request - please check your parameters" when it talks to LM Studio. The model is loaded and the URL is right. What else could it be?

**In one sentence:** n8n talks to **Ollama** with the *Ollama Chat Model* node, and to **LM Studio** with the *OpenAI Chat Model* node pointed at LM Studio, and almost every problem is one of five settings.

## 🪜 Ollama

Add a credential "Ollama" with the base URL from lesson 1 (for example `http://ollama:11434` in the starter kit). Pick the model in the *Ollama Chat Model* node.

## 🪜 LM Studio (OpenAI-compatible)

1. In LM Studio, start the server (Developer tab). If n8n is on another machine or in Docker, turn on **Serve on local network**.
2. In n8n, create an **OpenAI** credential: Base URL `http://host.docker.internal:1234/v1`, API key: a token from LM Studio (Settings → Authentication) or any placeholder text if authentication is off.
3. In the *OpenAI Chat Model* node, choose the model **By ID** and paste the exact ID from `http://localhost:1234/v1/models`.
4. Turn **off** "Use Responses API". LM Studio expects Chat Completions requests; the Responses API causes the "Bad request" error.

## 🔀 The five classic mistakes

<div class="wrong"><b>URL ends in <code>/chat/completions</code></b>: n8n adds that itself. Stop the URL at <code>/v1</code>.</div>
<div class="wrong"><b>LM Studio URL without <code>/v1</code></b>: the OpenAI node needs it.</div>
<div class="wrong"><b><code>localhost</code> while n8n is in Docker</b>: that's the container (lesson 1).</div>
<div class="wrong"><b>Responses API on with LM Studio</b>: "Bad request".</div>
<div class="wrong"><b>No model ID</b>: LM Studio doesn't know which model you mean.</div>
<div class="right">Base URL ending in <code>/v1</code>, right host, Responses API off, exact model ID ✓</div>

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `cfg["base_url"]` | "cfg at base URL" | the URL from the settings dictionary |
| `s.rstrip("/")` | "s, right-strip slash" | removes `/` from the **end** only: `"…/v1/"` → `"…/v1"` |
| `s.endswith("/v1")` | "s ends with slash v1" | `True` or `False` |
| `x == False` | "x is false" | true when `x` is `False`. So `url.endswith("/v1") == False` means "the URL does **not** end with /v1". |
| `"localhost" in url` | "localhost is in the URL" | true when that text appears anywhere inside `url` |
| `a and b` | "a and b" | true only when **both** are true |
| `a or b` | "a or b" | true when **at least one** is true |
| `a and (b or c)` | | the brackets are worked out first, like in maths |
| `problems.append("...")` | | adds one message to the list |

Several separate `if`s in a row are **all** checked, one after another. That's what we want: one setup can have many problems. Only rules 1 and 2 are joined with `elif`, because a URL that's too long (rule 1) doesn't also need "add /v1".

### 👀 Worked example: a packing checker

```python
def packing_problems(bag):
    problems = []
    if bag["weather"] == "rain" and bag["umbrella"] == False:
        problems.append("pack an umbrella")
    if bag["days"] > 3 or bag["flight"]:
        problems.append("bring the big bag")
    if bag["ticket"] == "":
        problems.append("print your ticket")
    return problems

print(packing_problems({"weather": "rain", "umbrella": False, "days": 2, "flight": True, "ticket": ""}))
```

1. Rain **and** no umbrella: both true → `"pack an umbrella"`.
2. `2 > 3` is false, but `flight` is true. With `or`, one is enough → `"bring the big bag"`.
3. The ticket is empty text `""` → `"print your ticket"`.
4. All three `if`s ran, so you get all three messages, in order.

## 🎯 Your quest

Write `setup_problems(cfg)` for an OpenAI-node-to-LM-Studio setup. `cfg` has `base_url`, `n8n_in_docker`, `use_responses_api` and `model`. Each rule below adds its exact message. Replace `return []` with:

1. `url = cfg["base_url"].rstrip("/")`
2. `problems = []`
3. Rules 1 and 2:
   - `if url.endswith("/chat/completions"):`
   - `    problems.append("cut the URL at /v1")`
   - `elif url.endswith("/v1") == False:`
   - `    problems.append("add /v1 to the URL")`
4. Rule 3:
   - `if cfg["n8n_in_docker"] and ("localhost" in url or "127.0.0.1" in url):`
   - `    problems.append("use host.docker.internal")`
5. Rule 4:
   - `if cfg["use_responses_api"]:`
   - `    problems.append("turn off Use Responses API")`
6. Rule 5:
   - `if cfg["model"] == "":`
   - `    problems.append("set the model ID")`
7. `return problems`

**Remember:** `/v1`, right host, Chat Completions, exact ID.

## Review

<details><summary>Lesson 5: which Code node mode sees all items at once?</summary>Run Once for All Items.</details>
<details><summary>What's the difference between two ifs in a row and an if with an elif?</summary>Two ifs are both checked. An elif is only checked when the if above it was false.</details>
