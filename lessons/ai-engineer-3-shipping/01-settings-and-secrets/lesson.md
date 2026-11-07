---
title: Settings and secrets
minutes: 40
xp: 45
hint: convert: if kind is bool: return text.strip().lower() in ["1", "true", "yes", "on"]. Otherwise return kind(text)
hint: load_settings, first loop: for name in spec: kind, default = spec[name], and if default is REQUIRED and name not in env: missing.append(name)
hint: Then: if len(missing) > 0: raise ValueError("missing settings: " + ", ".join(sorted(missing)))
hint: Second loop: out[name] = convert(kind, env[name]) if the name is in env, else out[name] = default
hint: safe_view: for k in settings: if k.endswith("_KEY") or k.endswith("_TOKEN") or k.endswith("_PASSWORD"): out[k] = "****"
---
# Config lives outside the code

⏱️ About 40 minutes

> **Warm-up:** where would you put an API key so your code can use it but GitHub never sees it?

Production apps read their settings from **environment variables** (or a `.env` file loaded into them), never from values typed into the code. That way the same code runs on your laptop, in Docker and on a server with different settings, and **secrets** (API keys, passwords) never end up in git.

Rules every AI engineer follows:

1. Secrets only in env vars or a secret manager. `.env` goes into `.gitignore`. Commit a `.env.example` with fake values instead.
2. **Fail fast:** if a required setting is missing, stop at startup with a clear message, not after 3 hours with a confusing error.
3. **Never log secrets.** When printing settings for debugging, mask them: `sk-abc…` → `****`.
4. Convert types once, at startup: env vars are always text (`"0.2"`, `"true"`).

If a key ever lands in a public repo, assume it's stolen: **revoke it** immediately; deleting the commit isn't enough (bots scan GitHub within minutes).

## 🧮 Worked example

All four rules in five lines:

```python
import os
temperature = float(os.environ.get("TEMPERATURE", "0.2"))  # rule 4: text → number, once, at startup
api_key = os.environ.get("API_KEY")
if not api_key:
    raise SystemExit("API_KEY is missing. Copy .env.example to .env and fill it in.")  # rule 2: fail fast
print("key:", api_key[:3] + "****")  # rule 3: never print the whole secret
```

And rule 1: the real key lives only in `.env` (which is in `.gitignore`); git only ever sees `.env.example` with `API_KEY=put-your-key-here`.

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `kind, default = spec[name]` | | each setting is a pair (type, default); this unpacks it |
| `kind is bool` | "kind is bool" | true when the type is exactly `bool`. `is` checks "the very same thing". |
| `kind(text)` | | the type used as a function: `int("512")` is 512, `float("0.2")` is 0.2, `str("x")` is "x" |
| `text.strip().lower() in [...]` | | `" Yes "` → `"yes"` → is it one of the yes-words? |
| `default is REQUIRED` | | `REQUIRED` is a special marker object (given); `is` checks for exactly that object |
| `raise ValueError("...")` | | stops with an error message |
| `", ".join(sorted(missing))` | | `["B", "A"]` → `"A, B"` |
| `k.endswith("_KEY")` | | true for `OPENAI_API_KEY` |

### 👀 Worked example: three settings

`env = {"OPENAI_API_KEY": "sk-secret", "DEBUG": "yes"}`:

1. Missing check: only `OPENAI_API_KEY` is required, and it's in env → `missing` stays empty, no error.
2. `MODEL` is not in env → its default `"llama3.2"`.
3. `DEBUG` is in env → `convert(bool, "yes")` → `"yes"` is a yes-word → **True**.
4. `OPENAI_API_KEY` → `convert(str, "sk-secret")` → `"sk-secret"`.
5. `safe_view` then shows `"OPENAI_API_KEY": "****"`, so the key never ends up in a log.

## 🎯 Your quest

`SPEC` (in the starter) describes each setting: `(type, default)`; a default of `REQUIRED` means it must be set. Names ending in `_KEY`, `_TOKEN` or `_PASSWORD` are secrets.

1. `load_settings(env, spec=SPEC)`: return a dict of converted values. Types: `str`, `int`, `float` and `bool` (`"1"`, `"true"`, `"yes"`, `"on"` → True, case-insensitive; anything else False). Missing required settings: raise `ValueError` whose message lists **all** missing names, sorted, like `"missing settings: A, B"`.
2. `safe_view(settings)`: a copy where every secret value is replaced by `"****"`.

The starter has a small helper `convert(kind, text)` for you to fill in first.

**Part 1:** `convert`. Replace `return text` with:

1. `if kind is bool:`
2. `    return text.strip().lower() in ["1", "true", "yes", "on"]`
3. `return kind(text)`

**Part 2:** `load_settings`. Replace `return {}` with:

1. `missing = []`
2. `for name in spec:`
3. `    kind, default = spec[name]`
4. `    if default is REQUIRED and name not in env:`
5. `        missing.append(name)`
6. `if len(missing) > 0:`
7. `    raise ValueError("missing settings: " + ", ".join(sorted(missing)))`
8. `out = {}`
9. `for name in spec:`
10. `    kind, default = spec[name]`
11. `    if name in env:`
12. `        out[name] = convert(kind, env[name])`
13. `    else:`
14. `        out[name] = default`
15. `return out`

**Part 3:** `safe_view`. Replace `return settings` with:

1. `out = {}`
2. `for k in settings:`
3. `    if k.endswith("_KEY") or k.endswith("_TOKEN") or k.endswith("_PASSWORD"):`
4. `        out[k] = "****"`
5. `    else:`
6. `        out[k] = settings[k]`
7. `return out`

**Remember:** env vars in, fail fast, mask secrets.

## Review

<details><summary>What is hybrid search?</summary>Keyword (BM25) and embedding search combined, usually with reciprocal rank fusion.</details>
