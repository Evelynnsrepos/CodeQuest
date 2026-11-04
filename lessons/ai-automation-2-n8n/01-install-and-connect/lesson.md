---
title: Install n8n and find your model
xp: 25
---
# Where does n8n look for your model?

⏱️ About 12 minutes · one function

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

## 🎯 Your quest

Write `model_url(n8n_in_docker, model_in_compose, service, port)` that returns `"http://HOST:PORT"` using the table:

- `model_url(False, False, "ollama", 11434)` → `"http://localhost:11434"`
- `model_url(True, True, "ollama", 11434)` → `"http://ollama:11434"`
- `model_url(True, False, "lmstudio", 1234)` → `"http://host.docker.internal:1234"`

<details><summary>💡 Hint</summary>Pick <code>host</code> with an if/elif/else: not in Docker → <code>"localhost"</code>; in the same compose file → <code>service</code>; else <code>"host.docker.internal"</code>.</details>

**Remember:** in Docker, `localhost` is the container.

## Review

<details><summary>AI automation 1, lesson 8: what does "idempotent" mean?</summary>Running it twice does no extra harm: done items are skipped.</details>
