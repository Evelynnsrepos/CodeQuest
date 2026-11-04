def load_order(cwd, existing, home):
    return []


def imports(text):
    return []


def index_loaded(lines):
    return lines


ex = {"/home/eve/.claude/CLAUDE.md", "/home/eve/CodeQuest/CLAUDE.md", "/home/eve/CodeQuest/CLAUDE.local.md", "/home/eve/CodeQuest/lessons/CLAUDE.md"}
print(load_order("/home/eve/CodeQuest/lessons", ex, "/home/eve"))
print(imports("See @docs/testing.md and `@README` and @~/notes.md"))
