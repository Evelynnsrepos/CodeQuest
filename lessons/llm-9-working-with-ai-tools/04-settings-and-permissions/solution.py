def matches(rule, tool, command):
    if "(" not in rule:
        return rule == tool
    name, pattern = rule[:-1].split("(", 1)
    if name != tool:
        return False
    for tail in (" *", ":*"):
        if pattern.endswith(tail):
            prefix = pattern[: -len(tail)]
            return command == prefix or command.startswith(prefix + " ")
    if pattern.endswith("*"):
        return command.startswith(pattern[:-1])
    return command == pattern


def decide(tool, command, rules):
    for outcome in ("deny", "ask", "allow"):
        if any(matches(r, tool, command) for r in rules.get(outcome, [])):
            return outcome
    return "ask"


def effective(key, layers):
    for name in ("managed", "cli", "local", "project", "user"):
        if key in layers.get(name, {}):
            return layers[name][key]
    return None


rules = {"deny": ["Bash(git push *)"], "allow": ["Bash(git *)"]}
print(decide("Bash", "git status", rules), decide("Bash", "git push origin main", rules), decide("Bash", "npm install", rules))
