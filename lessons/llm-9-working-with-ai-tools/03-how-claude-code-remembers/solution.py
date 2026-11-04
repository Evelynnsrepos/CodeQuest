import re


def load_order(cwd, existing, home):
    out = []
    user = home + "/.claude/CLAUDE.md"
    if user in existing:
        out.append(user)
    parts = [p for p in cwd.split("/") if p]
    folders = ["/" + "/".join(parts[:i]) for i in range(len(parts) + 1)]
    for folder in folders:
        base = folder.rstrip("/")
        for name in ("CLAUDE.md", ".claude/CLAUDE.md", "CLAUDE.local.md"):
            path = base + "/" + name
            if path in existing and path not in out:
                out.append(path)
    return out


def imports(text):
    text = re.sub(r"`[^`]*`", "", text)
    return re.findall(r"(?:^|(?<=\s))@(\S+)", text)


def index_loaded(lines):
    out, size = [], 0
    for line in lines[:200]:
        size += len(line) + 1
        if size > 25000:
            break
        out.append(line)
    return out


ex = {"/home/eve/.claude/CLAUDE.md", "/home/eve/CodeQuest/CLAUDE.md", "/home/eve/CodeQuest/CLAUDE.local.md", "/home/eve/CodeQuest/lessons/CLAUDE.md"}
print(load_order("/home/eve/CodeQuest/lessons", ex, "/home/eve"))
print(imports("See @docs/testing.md and `@README` and @~/notes.md"))
