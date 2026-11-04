import re


def guard(event):
    return (0, "")


def matcher_hits(matcher, tool_name):
    return True


print(guard({"tool_name": "Bash", "tool_input": {"command": "rm -rf build"}}), matcher_hits("Edit|Write", "Bash"))
