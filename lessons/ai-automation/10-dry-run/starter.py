def execute(actions, tools, dry_run=True):
    # log = []
    # for action in actions:
    #     name = action["tool"]
    #     args = action["args"]
    #     parts = []
    #     for key in args:
    #         parts.append(key + "=" + repr(args[key]))
    #     if dry_run:
    #         prefix = "DRY"
    #     else:
    #         prefix = "RAN"
    #         tools[name](**args)
    #     log.append(prefix + " " + name + "(" + ", ".join(parts) + ")")
    # return log
    log = []
    for action in actions:
        tools[action["tool"]](**action["args"])
    return log


renamed = []


def rename(old, new):
    renamed.append(old + " -> " + new)


tools = {"rename": rename}
actions = [{"tool": "rename", "args": {"old": "IMG_001.jpg", "new": "2026-11-04 beach.jpg"}}]
for line in execute(actions, tools):
    print(line)
print("renamed:", renamed)
