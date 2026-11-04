---
title: Settings and secrets
xp: 45
---
# Config lives outside the code

> **Warm-up:** where would you put an API key so your code can use it but GitHub never sees it?

Production apps read their settings from **environment variables** (or a `.env` file loaded into them), never from values typed into the code. That way the same code runs on your laptop, in Docker and on a server with different settings, and **secrets** (API keys, passwords) never end up in git.

Rules every AI engineer follows:

1. Secrets only in env vars or a secret manager. `.env` goes into `.gitignore`. Commit a `.env.example` with fake values instead.
2. **Fail fast:** if a required setting is missing, stop at startup with a clear message, not after 3 hours with a confusing error.
3. **Never log secrets.** When printing settings for debugging, mask them: `sk-abc…` → `****`.
4. Convert types once, at startup: env vars are always text (`"0.2"`, `"true"`).

If a key ever lands in a public repo, assume it's stolen: **revoke it** immediately; deleting the commit isn't enough (bots scan GitHub within minutes).

## Your quest

`SPEC` (in the starter) describes each setting: `(type, default)`; a default of `REQUIRED` means it must be set. Names ending in `_KEY`, `_TOKEN` or `_PASSWORD` are secrets.

1. `load_settings(env, spec=SPEC)`: return a dict of converted values. Types: `str`, `int`, `float` and `bool` (`"1"`, `"true"`, `"yes"`, `"on"` → True, case-insensitive; anything else False). Missing required settings: raise `ValueError` whose message lists **all** missing names, sorted, like `"missing settings: A, B"`.
2. `safe_view(settings)`: a copy where every secret value is replaced by `"****"`.

**Remember:** env vars in, fail fast, mask secrets.

## Review

<details><summary>What is hybrid search?</summary>Keyword (BM25) and embedding search combined, usually with reciprocal rank fusion.</details>
