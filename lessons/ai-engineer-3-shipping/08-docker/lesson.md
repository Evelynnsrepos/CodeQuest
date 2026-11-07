---
title: Docker: ship it in a box
minutes: 50
xp: 60
hint: Part 1: lines = [], then for l in dockerfile.splitlines(): l = l.strip(), keep it if l != "" and not l.startswith("#")
hint: Part 2: find the FROM line, base = l.split()[1], then add "base" if ":" not in base or base.endswith(":latest") or not ("slim" in base or "alpine" in base)
hint: Part 3: remember the position i of the first "COPY . ." and of the first "pip install" line; "order" if copy_all < pip
hint: Part 4: four flags cache, root, secret, cmd set in one loop over the lines, then one if per flag
hint: Part 5: replace DOCKERFILE with the recipe at the top of the lesson (without the # notes) and DOCKERIGNORE with the four names, one per line
---
# "Works on my machine" → works everywhere

⏱️ About 50 minutes

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

## Python you need

| You write | Say it | What it does |
|---|---|---|
| `text.splitlines()` | | the text cut into a list of lines |
| `l.strip()` | | the line without spaces at the start and end |
| `l.startswith("#")` | | a comment line in a Dockerfile |
| `l.upper()` | | `"from x"` → `"FROM X"`, so lower-case instructions count too |
| `l.split()` | | cut at the spaces: `"FROM python:3.12-slim".split()` is `["FROM", "python:3.12-slim"]`, so `[1]` is the image name and `[0]` the instruction |
| `break` | | stop the loop now (we only want the **first** FROM) |
| `":" not in base` | | no tag: `python` instead of `python:3.12` |
| `base.endswith(":latest")` | | the tag is `latest` |
| `for i in range(len(lines)):` | | `i` = 0, 1, 2, … one for each line, so we know **where** a line is |
| `copy_all is None` | | "not found yet" (it starts as `None`) |
| `l.replace("  ", " ")` | | turns double spaces into single ones, so `COPY  . .` also counts |
| `for word in ["KEY", "TOKEN", "PASSWORD"]:` | | tries each of the three words |

### 👀 Worked example: the starter's bad Dockerfile

```
FROM python
COPY . .
RUN pip install -r requirements.txt
ENV OPENAI_API_KEY=sk-123
CMD ["uvicorn", "main:app"]
```

1. **base**: `base` = `"python"`, there's no `:` → problem.
2. **order**: `COPY . .` is line 0, `pip install` is line 1, 0 < 1 → problem (the code is copied before the packages are installed).
3. **cache**: the pip line has no `--no-cache-dir` → problem.
4. **root**: there's no `USER` line → problem.
5. **secret**: an `ENV` line with `KEY` in it → problem.
6. **host**: the `CMD` has no `0.0.0.0` → problem.

Result: `["base", "order", "cache", "root", "secret", "host"]`. The good Dockerfile at the top of the lesson gives `[]`.

## 🎯 Your quest

1. `lint(dockerfile)`: return a list of problem codes, in this order, for the rules: `"base"` (the `FROM` image has no tag, or uses `latest`, or isn't a `slim`/`alpine` variant), `"order"` (`COPY . .` comes before the `pip install` line), `"cache"` (a `pip install` without `--no-cache-dir`), `"root"` (no `USER` line), `"secret"` (an `ENV` line whose name contains `KEY`, `TOKEN` or `PASSWORD`), `"host"` (the `CMD` doesn't contain `0.0.0.0`).
2. Write `DOCKERFILE` (passing your lint) and `DOCKERIGNORE` (containing at least `.env`, `.git`, `.venv` and `__pycache__`, one per line).

Replace `return []` in `lint` with these lines (each part follows the one before).

**Part 1:** keep only the real lines (no empty lines, no comments):

1. `lines = []`
2. `for l in dockerfile.splitlines():`
3. `    l = l.strip()`
4. `    if l != "" and not l.startswith("#"):`
5. `        lines.append(l)`

**Part 2:** the base image:

6. `problems = []`
7. `base = ""`
8. `for l in lines:`
9. `    if l.upper().startswith("FROM "):`
10. `        base = l.split()[1]`
11. `        break`
12. `if ":" not in base or base.endswith(":latest") or not ("slim" in base or "alpine" in base):`
13. `    problems.append("base")`

**Part 3:** the order of `COPY . .` and `pip install`:

14. `copy_all = None`
15. `pip = None`
16. `for i in range(len(lines)):`
17. `    if copy_all is None and lines[i].replace("  ", " ") == "COPY . .":`
18. `        copy_all = i`
19. `    if pip is None and "pip install" in lines[i]:`
20. `        pip = i`
21. `if copy_all is not None and pip is not None and copy_all < pip:`
22. `    problems.append("order")`

**Part 4:** the other four rules, all found in one loop:

23. `cache = False`
24. `root = True`
25. `secret = False`
26. `cmd = ""`
27. `for l in lines:`
28. `    first = l.split()[0].upper()`
29. `    if "pip install" in l and "--no-cache-dir" not in l:`
30. `        cache = True`
31. `    if first == "USER":`
32. `        root = False`
33. `    if first == "ENV":`
34. `        for word in ["KEY", "TOKEN", "PASSWORD"]:`
35. `            if word in l.upper():`
36. `                secret = True`
37. `    if first == "CMD" and cmd == "":`
38. `        cmd = l`
39. `if cache:`
40. `    problems.append("cache")`
41. `if root:`
42. `    problems.append("root")`
43. `if secret:`
44. `    problems.append("secret")`
45. `if "0.0.0.0" not in cmd:`
46. `    problems.append("host")`
47. `return problems`

**Part 5:** replace the starter's `DOCKERFILE` with the good recipe from the top of this lesson (the `# ...` notes on the right are only explanations, leave them out), and set `DOCKERIGNORE` to:

```
DOCKERIGNORE = """.env
.git
.venv
__pycache__
*.pyc
"""
```

**Remember:** slim pinned base, dependencies first, non-root, no secrets, 0.0.0.0.

## Review

<details><summary>Why only cache temperature-0 calls?</summary>Caching a random answer freezes it; deterministic calls give the same answer anyway.</details>
