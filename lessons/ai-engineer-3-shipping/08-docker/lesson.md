---
title: Docker: ship it in a box
xp: 60
---
# "Works on my machine" → works everywhere

> **Warm-up:** your app needs Python 3.12, eight packages and two environment variables. How do you make it run the same way on a server?

**Docker** packs your app, its Python and its packages into an **image**. Anyone with Docker runs it the same way: `docker run -p 8000:8000 --env-file .env myapp`. A **Dockerfile** is the recipe:

```dockerfile
FROM python:3.12-slim                 # small official base image, pinned version
WORKDIR /app
COPY requirements.txt .               # 1. dependencies first...
RUN pip install --no-cache-dir -r requirements.txt
COPY . .                              # 2. ...then your code
RUN useradd --create-home appuser
USER appuser                          # don't run as root
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Why each line matters:

| Rule | Why |
|---|---|
| a **slim**, **versioned** base (`python:3.12-slim`, never `latest`) | smaller, faster, reproducible |
| copy `requirements.txt` and install **before** `COPY . .` | Docker caches each step; editing code then doesn't reinstall every package |
| `--no-cache-dir` | pip's download cache would bloat the image |
| a non-root `USER` | if someone breaks in, they're not root in the container |
| `--host 0.0.0.0` | `127.0.0.1` inside a container isn't reachable from outside |
| **no secrets** in the Dockerfile (`ENV API_KEY=...`) | anyone with the image can read them; pass them at run time |

A `.dockerignore` keeps junk and secrets out of `COPY . .`: at least `.env`, `.git`, `.venv` and `__pycache__`.

Build and run: `docker build -t myapp .` then `docker run --rm -p 8000:8000 --env-file .env myapp`.

## Your quest

1. `lint(dockerfile)`: return a list of problem codes, in this order, for the rules: `"base"` (the `FROM` image has no tag, or uses `latest`, or isn't a `slim`/`alpine` variant), `"order"` (`COPY . .` comes before the `pip install` line), `"cache"` (a `pip install` without `--no-cache-dir`), `"root"` (no `USER` line), `"secret"` (an `ENV` line whose name contains `KEY`, `TOKEN` or `PASSWORD`), `"host"` (the `CMD` doesn't contain `0.0.0.0`).
2. Write `DOCKERFILE` (passing your lint) and `DOCKERIGNORE` (containing at least `.env`, `.git`, `.venv` and `__pycache__`, one per line).

**Remember:** slim pinned base, dependencies first, non-root, no secrets, 0.0.0.0.

## Review

<details><summary>Why only cache temperature-0 calls?</summary>Caching a random answer freezes it; deterministic calls give the same answer anyway.</details>
