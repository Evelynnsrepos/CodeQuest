li, DF, DI = ns.get("lint"), ns.get("DOCKERFILE"), ns.get("DOCKERIGNORE")
assert li and DF and DI is not None, "Keep lint, DOCKERFILE and DOCKERIGNORE."
bad = """FROM python
COPY . .
RUN pip install -r requirements.txt
ENV OPENAI_API_KEY=sk-123
CMD ["uvicorn", "main:app"]
"""
assert li(bad) == ["base", "order", "cache", "root", "secret", "host"], f"The bad Dockerfile breaks every rule. Got {li(bad)!r}."
good = """FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd --create-home appuser
USER appuser
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""
assert li(good) == [], f"The good example passes. Got {li(good)!r}."
assert li(good.replace("python:3.12-slim", "python:latest")) == ["base"], "latest is not a pinned slim base."
assert li(good.replace("python:3.12-slim", "python:3.12")) == ["base"], "Use a slim or alpine variant."
assert li(good.replace("ENV", "ENV").replace("EXPOSE 8000", "ENV LOG_LEVEL=info\nEXPOSE 8000")) == [], "A harmless ENV is fine."
assert li(DF) == [], f"Your DOCKERFILE should pass your lint. Problems: {li(DF)!r}."
lines = {l.strip() for l in DI.splitlines()}
assert {".env", ".git", ".venv", "__pycache__"} <= lines, "DOCKERIGNORE needs .env, .git, .venv and __pycache__."
