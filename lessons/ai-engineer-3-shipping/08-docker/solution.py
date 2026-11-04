def lint(dockerfile):
    lines = [l.strip() for l in dockerfile.splitlines() if l.strip() and not l.strip().startswith("#")]
    upper = [l.split()[0].upper() for l in lines]
    problems = []
    base = next((l.split()[1] for l in lines if l.upper().startswith("FROM ")), "")
    if ":" not in base or base.endswith(":latest") or not ("slim" in base or "alpine" in base):
        problems.append("base")
    copy_all = next((i for i, l in enumerate(lines) if l.replace("  ", " ") == "COPY . ."), None)
    pip = next((i for i, l in enumerate(lines) if "pip install" in l), None)
    if copy_all is not None and pip is not None and copy_all < pip:
        problems.append("order")
    if any("pip install" in l and "--no-cache-dir" not in l for l in lines):
        problems.append("cache")
    if "USER" not in upper:
        problems.append("root")
    if any(u == "ENV" and any(w in l.upper() for w in ("KEY", "TOKEN", "PASSWORD")) for u, l in zip(upper, lines)):
        problems.append("secret")
    cmd = next((l for u, l in zip(upper, lines) if u == "CMD"), "")
    if "0.0.0.0" not in cmd:
        problems.append("host")
    return problems


DOCKERFILE = """FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
RUN useradd --create-home appuser
USER appuser
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
"""

DOCKERIGNORE = """.env
.git
.venv
__pycache__
*.pyc
"""

print(lint(DOCKERFILE))
