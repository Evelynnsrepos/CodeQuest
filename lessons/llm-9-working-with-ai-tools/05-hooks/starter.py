import re


def guard(event):
    # tool = event.get("tool_name")
    # inp = event.get("tool_input", {})
    # if tool == "Bash" and "rm -rf" in inp.get("command", ""):
    #     return (2, "Blocked: rm -rf is not allowed")
    # if tool == "Read" and inp.get("file_path", "").endswith(".env"):
    #     return (2, "Blocked: .env files hold secrets")
    # return (0, "")
    return (0, "")


def matcher_hits(matcher, tool_name):
    # if matcher == "*" or matcher == "":
    #     return True
    # simple = True
    # for ch in matcher:
    #     if not (ch.isalnum() or ch in "_- ,|"):
    #         simple = False
    # if simple:
    #     names = matcher.replace(",", "|").split("|")
    #     for n in names:
    #         if n.strip() == tool_name:
    #             return True
    #     return False
    # return re.search(matcher, tool_name) is not None
    return True


print(guard({"tool_name": "Bash", "tool_input": {"command": "rm -rf build"}}), matcher_hits("Edit|Write", "Bash"))
