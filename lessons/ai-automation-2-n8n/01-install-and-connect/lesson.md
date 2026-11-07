---
title: Install n8n and find your model
minutes: 20
xp: 25
hint: First the if: if n8n_in_docker == False: and under it host = "localhost"
hint: Then elif model_in_compose: and under it host = service, then else: and under it host = "host.docker.internal"
hint: Last line: return "http://" + host + ":" + str(port)
---
# Where does n8n look for your model?

⏱️ About 20 minutes · one function, seven lines

> **Warm-up:** n8n runs in Docker, LM Studio runs on your normal desktop. n8n calls `http://localhost:1234` and gets "connection refused". LM Studio is running. Why?

**In one sentence:** n8n is a web app (at `http://localhost:5678`) where you build automations by connecting **nodes**, and the most common first problem is giving it the wrong address for your local model.

## 🪜 Three ways to run n8n

| Way | Command | Good for |
|---|---|---|
| Plain Docker | `docker volume create n8n_data` then `docker run -it --rm --name n8n -p 5678:5678 -v n8n_data:/home/node/.n8n docker.n8n.io/n8nio/n8n` | trying it |
| AI starter kit | `git clone https://github.com/n8n-io/self-hosted-ai-starter-kit.git`, `cd` into it, `cp .env.example .env` (change the passwords in it), then `docker compose --profile gpu-amd up` | n8n + Ollama + Qdrant + Postgres in one go, on your AMD GPU (Linux) |
| NixOS | `services.n8n.enable = true;` in your config (add `services.n8n.openFirewall = true;` for your phone) | your own machine, no Docker |

The starter kit says itself it's for testing, not production. On NixOS, n8n's licence counts as "unfree", so if the build complains, allow it like you did for other unfree packages.

## 🪜 The address puzzle

Inside a Docker container, `localhost` means **the container itself**, not your computer. So:

| n8n runs… | model runs… | n8n must call |
|---|---|---|
| on your computer | on your computer | `localhost` |
| in Docker | in the same compose file (starter kit) | the service name, e.g. `ollama` |
| in Docker | on your computer (LM Studio, or Ollama outside Docker) | `host.docker.internal` |

Ports: Ollama uses **11434**, LM Studio **1234**, n8n **5678**.

On Linux, `host.docker.internal` only works if the container was started with `--add-host=host.docker.internal:host-gateway` (Docker Desktop on Windows and Mac adds it for you).

## 🐍 Python you need

| You write | Say it | What it does |
|---|---|---|
| `True`, `False` | "true", "false" | Python's yes and no. Here they answer "is n8n in Docker?" and "is the model in the same compose file?" |
| `if x == False:` | "if x is false" | the lines under it run only when `x` is `False` |
| `elif y:` | "else if y" | checked only if the `if` above was false. Runs when `y` is `True`. |
| `else:` | "else" | runs when nothing above it was true |
| `host = service` | "host becomes service" | copies the text from the box `service` into the box `host` |
| `str(1234)` | "string of 1234" | turns the number into the text `"1234"`, so you can glue it to other text with `+` |
| `"http://" + host` | | glues texts together |

### 👀 Worked example: which door to use

Same shape: three cases, checked from top to bottom, the first one that's true wins.

```python
def door(raining, has_key, name):
    if raining == False:
        way = "garden"
    elif has_key:
        way = name
    else:
        way = "doorbell"
    return "go via " + way + " door " + str(1)
```

`door(True, False, "back")`:

1. `raining == False`? `raining` is `True`, so no. Skip that block.
2. `elif has_key:` is `has_key` true? No, it's `False`. Skip.
3. `else:` nothing above was true, so `way = "doorbell"`.
4. Returns `"go via doorbell door 1"`.

`door(True, True, "back")`: step 2 is true, so `way` = `"back"` → `"go via back door 1"`.

## 🎯 Your quest

Write `model_url(n8n_in_docker, model_in_compose, service, port)`. It follows the address table from top to bottom. Replace the starter's line with:

1. `if n8n_in_docker == False:`
2. `    host = "localhost"`
3. `elif model_in_compose:`
4. `    host = service`
5. `else:`
6. `    host = "host.docker.internal"`
7. `return "http://" + host + ":" + str(port)`

It should give:

- `model_url(False, False, "ollama", 11434)` → `"http://localhost:11434"`
- `model_url(True, True, "ollama", 11434)` → `"http://ollama:11434"`
- `model_url(True, False, "lmstudio", 1234)` → `"http://host.docker.internal:1234"`

**Remember:** in Docker, `localhost` is the container.

## Review

<details><summary>AI automation 1, lesson 8: what does "idempotent" mean?</summary>Running it twice does no extra harm: done items are skipped.</details>
<details><summary>Why does the order of if, elif and else matter here?</summary>Python checks them from top to bottom and uses the first true one. If n8n isn't in Docker, it's localhost, no matter where the model is.</details>
