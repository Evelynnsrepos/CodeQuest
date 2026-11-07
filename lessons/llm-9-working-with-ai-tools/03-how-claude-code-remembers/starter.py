def load_order(cwd, existing, home):
    # out = []
    # user = home + "/.claude/CLAUDE.md"
    # if user in existing:
    #     out.append(user)
    # folders = [""]
    # folder = ""
    # for part in cwd.split("/"):
    #     if part != "":
    #         folder = folder + "/" + part
    #         folders.append(folder)
    # for folder in folders:
    #     for name in ["CLAUDE.md", ".claude/CLAUDE.md", "CLAUDE.local.md"]:
    #         path = folder + "/" + name
    #         if path in existing and path not in out:
    #             out.append(path)
    # return out
    return []


def imports(text):
    # out = []
    # pieces = text.split("`")
    # for i in range(0, len(pieces), 2):
    #     for word in pieces[i].split():
    #         if word.startswith("@"):
    #             out.append(word[1:])
    # return out
    return []


def index_loaded(lines):
    # out = []
    # size = 0
    # for line in lines[:200]:
    #     size = size + len(line) + 1
    #     if size > 25000:
    #         break
    #     out.append(line)
    # return out
    return lines


ex = {"/home/eve/.claude/CLAUDE.md", "/home/eve/CodeQuest/CLAUDE.md", "/home/eve/CodeQuest/CLAUDE.local.md", "/home/eve/CodeQuest/lessons/CLAUDE.md"}
print(load_order("/home/eve/CodeQuest/lessons", ex, "/home/eve"))
print(imports("See @docs/testing.md and `@README` and @~/notes.md"))
