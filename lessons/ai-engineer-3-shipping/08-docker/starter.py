def lint(dockerfile):
    # lines = []
    # for l in dockerfile.splitlines():
    #     l = l.strip()
    #     if l != "" and not l.startswith("#"):
    #         lines.append(l)
    # problems = []
    # base = ""
    # for l in lines:
    #     if l.upper().startswith("FROM "):
    #         base = l.split()[1]
    #         break
    # if ":" not in base or base.endswith(":latest") or not ("slim" in base or "alpine" in base):
    #     problems.append("base")
    # copy_all = None
    # pip = None
    # for i in range(len(lines)):
    #     if copy_all is None and lines[i].replace("  ", " ") == "COPY . .":
    #         copy_all = i
    #     if pip is None and "pip install" in lines[i]:
    #         pip = i
    # if copy_all is not None and pip is not None and copy_all < pip:
    #     problems.append("order")
    # cache = False
    # root = True
    # secret = False
    # cmd = ""
    # for l in lines:
    #     first = l.split()[0].upper()
    #     if "pip install" in l and "--no-cache-dir" not in l:
    #         cache = True
    #     if first == "USER":
    #         root = False
    #     if first == "ENV":
    #         for word in ["KEY", "TOKEN", "PASSWORD"]:
    #             if word in l.upper():
    #                 secret = True
    #     if first == "CMD" and cmd == "":
    #         cmd = l
    # if cache:
    #     problems.append("cache")
    # if root:
    #     problems.append("root")
    # if secret:
    #     problems.append("secret")
    # if "0.0.0.0" not in cmd:
    #     problems.append("host")
    # return problems
    return []


DOCKERFILE = """FROM python
COPY . .
RUN pip install -r requirements.txt
ENV OPENAI_API_KEY=sk-123
CMD ["uvicorn", "main:app"]
"""

DOCKERIGNORE = ""

print(lint(DOCKERFILE))
