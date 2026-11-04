g, mh = ns.get("guard"), ns.get("matcher_hits")
assert g and mh, "Keep guard and matcher_hits."
code, err = g({"tool_name": "Bash", "tool_input": {"command": "rm -rf build"}})
assert code == 2 and err, f"rm -rf must be blocked with exit 2 and a reason, got {(code, err)!r}."
assert g({"tool_name": "Bash", "tool_input": {"command": "ls -la"}}) == (0, ""), "Safe commands pass with (0, '')."
assert g({"tool_name": "Read", "tool_input": {"file_path": "/repo/.env"}})[0] == 2, "Reading .env must be blocked."
assert g({"tool_name": "Read", "tool_input": {"file_path": "/repo/main.py"}}) == (0, ""), "Other reads pass."
assert g({"tool_name": "Edit", "tool_input": {"file_path": "x.env"}}) == (0, ""), "Only Read of .env is blocked here."
assert mh("*", "Bash") and mh("", "Edit"), "* and empty match everything."
assert mh("Edit|Write", "Write") and not mh("Edit|Write", "Bash"), "Exact list."
assert mh("Bash", "Bash") and not mh("Bash", "BashOutput"), "Plain name = exact, not prefix."
assert mh("mcp__memory__.*", "mcp__memory__save") and not mh("mcp__memory__.*", "mcp__github__x"), "Other characters → regex."
assert mh("^Notebook", "NotebookEdit"), "Regex anchors work."
