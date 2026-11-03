import posixpath


def is_allowed(path, root):
    full = posixpath.normpath(posixpath.join(root, path))
    return full == root or full.startswith(root + "/")


def lethal_trifecta(tools):
    have = set()
    for capabilities in tools:
        have = have | capabilities
    return {"private_data", "untrusted_input", "sends_out"} <= have


root = "/home/evilynn/notes"
for p in ["todo.md", "2026/november.md", "../.ssh/id_ed25519", "/etc/passwd",
          "/home/evilynn/notes-private/diary.md", "sub/../../notes/ok.md"]:
    print(f"{p:40} {is_allowed(p, root)}")

browser = {"untrusted_input", "sends_out"}
notes = {"private_data"}
print("notes + browser:", lethal_trifecta([notes, browser]))
print("notes only:     ", lethal_trifecta([notes]))
