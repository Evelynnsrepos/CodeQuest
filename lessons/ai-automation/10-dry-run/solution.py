def execute(actions, tools, dry_run=True):
    log = []
    prefix = "DRY" if dry_run else "RAN"
    for a in actions:
        name, args = a["tool"], a["args"]
        args_text = ", ".join(f"{k}={v!r}" for k, v in args.items())
        if not dry_run:
            tools[name](**args)
        log.append(f"{prefix} {name}({args_text})")
    return log


renamed = []
tools = {"rename": lambda old, new: renamed.append((old, new))}
actions = [{"tool": "rename", "args": {"old": "IMG_001.jpg", "new": "2026-11-04 beach.jpg"}}]
for line in execute(actions, tools):
    print(line)
print("renamed:", renamed)
