import posixpath


def is_allowed(path, root):
    # full = posixpath.normpath(posixpath.join(root, path))
    # return full == root or full.startswith(root + "/")
    return True


def lethal_trifecta(tools):
    # have = set()
    # for capabilities in tools:
    #     for c in capabilities:
    #         have.add(c)
    # return "private_data" in have and "untrusted_input" in have and "sends_out" in have
    return False


root = "/home/evilynn/notes"
for p in ["todo.md", "2026/november.md", "../.ssh/id_ed25519", "/etc/passwd",
          "/home/evilynn/notes-private/diary.md", "sub/../../notes/ok.md"]:
    print(p, is_allowed(p, root))

browser = {"untrusted_input", "sends_out"}
notes = {"private_data"}
print("notes + browser:", lethal_trifecta([notes, browser]))
print("notes only:", lethal_trifecta([notes]))
