def execute(actions, tools, dry_run=True):
    log = []
    for a in actions:
        tools[a["tool"]](**a["args"])
    return log


renamed = []
tools = {"rename": lambda old, new: renamed.append((old, new))}
actions = [{"tool": "rename", "args": {"old": "IMG_001.jpg", "new": "2026-11-04 beach.jpg"}}]
for line in execute(actions, tools):
    print(line)
print("renamed:", renamed)
