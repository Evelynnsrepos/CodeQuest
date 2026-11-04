---
title: Connect LM Studio and Ollama
xp: 30
---
# Fix the five classic setup mistakes

⏱️ About 12 minutes · one function

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

## 🎯 Your quest

Write `setup_problems(cfg)` for an OpenAI-node-to-LM-Studio setup. `cfg` has `base_url`, `n8n_in_docker`, `use_responses_api` and `model`. Return a list with these exact messages, in this order, for each problem found:

1. URL ends with `/chat/completions` → `"cut the URL at /v1"`
2. otherwise, URL doesn't end with `/v1` → `"add /v1 to the URL"`
3. `n8n_in_docker` and `"localhost"` or `"127.0.0.1"` in the URL → `"use host.docker.internal"`
4. `use_responses_api` → `"turn off Use Responses API"`
5. `model` is empty → `"set the model ID"`

Ignore a trailing `/` at the end of the URL (`.rstrip("/")`).

<details><summary>💡 Hint</summary>Start with <code>url = cfg["base_url"].rstrip("/")</code> and <code>problems = []</code>, then one <code>if</code> per rule (rules 1 and 2 are <code>if</code>/<code>elif</code>).</details>

**Remember:** `/v1`, right host, Chat Completions, exact ID.

## Review

<details><summary>Lesson 5: which Code node mode sees all items at once?</summary>Run Once for All Items.</details>
