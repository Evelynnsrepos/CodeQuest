import re


def guard(event):
    tool, inp = event.get("tool_name"), event.get("tool_input", {})
    if tool == "Bash" and "rm -rf" in inp.get("command", ""):
        return (2, "Blocked: rm -rf is not allowed")
    if tool == "Read" and inp.get("file_path", "").endswith(".env"):
        return (2, "Blocked: .env files hold secrets")
    return (0, "")


def matcher_hits(matcher, tool_name):
    if matcher in ("*", ""):
        return True
    if re.fullmatch(r"[A-Za-z0-9_\- ,|]+", matcher):
        return tool_name in [m.strip() for m in re.split(r"[|,]", matcher)]
    return re.search(matcher, tool_name) is not None


print(guard({"tool_name": "Bash", "tool_input": {"command": "rm -rf build"}}), matcher_hits("Edit|Write", "Bash"))
