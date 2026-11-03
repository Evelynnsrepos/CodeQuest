import json, posixpath
text = ns.get("MCP_JSON", "")
try:
    cfg = json.loads(text)
except ValueError as e:
    raise AssertionError(f"MCP_JSON isn't valid JSON yet: {e}. Check quotes (only double quotes), commas and brackets.")
assert isinstance(cfg, dict) and list(cfg) == ["mcpServers"], "The top level should have exactly one key: \"mcpServers\"."
servers = cfg["mcpServers"]
assert isinstance(servers, dict) and list(servers) == ["notes"], f"mcpServers should contain one server named \"notes\", found {list(servers) if isinstance(servers, dict) else servers!r}."
s = servers["notes"]
assert "url" not in s, "This is a local server: use command and args, not url."
cmd = s.get("command", "")
assert cmd == "npx" or cmd.endswith("/npx"), f"command should be npx (or a full path to npx), not {cmd!r}."
args = s.get("args")
assert isinstance(args, list) and all(isinstance(a, str) for a in args), "args must be a list of strings."
assert "-y" in args, "Add \"-y\" to args so npx doesn't stop to ask whether to install the package."
pkgs = [a for a in args if a.startswith("@modelcontextprotocol/server-filesystem")]
assert len(pkgs) == 1, "args should name the package @modelcontextprotocol/server-filesystem."
assert args.index("-y") < args.index(pkgs[0]), "\"-y\" is an npx option, so it goes before the package name."
folders = args[args.index(pkgs[0]) + 1:]
assert len(folders) == 1, f"After the package name, give exactly one folder. You gave {folders!r}."
folder = folders[0]
assert folder.startswith("/"), f"{folder!r} isn't an absolute path. Start it with / (the server doesn't expand ~)."
norm = posixpath.normpath(folder)
assert norm.count("/") >= 3 and not norm.startswith(("/etc", "/nix", "/run")), f"{folder!r} is too broad or a system folder. Point it at one folder inside your home, like /home/evilynn/llm-notes."
assert ns.get("transport") == "stdio", "transport: a server started from command and args talks over stdin/stdout."
assert ns.get("who_starts_it") == "lmstudio", "who_starts_it: with a stdio server, the client starts it from your config."
a = ns.get("if_command_not_found")
assert a == "b", {"a": "Reinstalling won't change the PATH an app launched from your desktop sees.",
                  "c": "That changes the whole setup; the problem is only that LM Studio can't find npx."}.get(a, "if_command_not_found: set it to \"a\", \"b\" or \"c\".")
