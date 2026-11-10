def matches(rule, tool, command):
    if "(" not in rule:
        return rule == tool
    i = rule.index("(")
    name = rule[:i]
    pattern = rule[i + 1:-1]
    if name != tool:
        return False
    if pattern.endswith(" *") or pattern.endswith(":*"):
        prefix = pattern[:-2]
        return command == prefix or command.startswith(prefix + " ")
    if pattern.endswith("*"):
        return command.startswith(pattern[:-1])
    return command == pattern


def decide(tool, command, rules):
    for outcome in ["deny", "ask", "allow"]:
        for rule in rules.get(outcome, []):
            if matches(rule, tool, command):
                return outcome
    return "ask"


def effective(key, layers):
    for name in ["managed", "cli", "local", "project", "user"]:
        settings = layers.get(name, {})
        if key in settings:
            return settings[key]
    return None


rules = {"deny": ["Bash(git push *)"], "allow": ["Bash(git *)"]}
print(decide("Bash", "git status", rules), decide("Bash", "git push origin main", rules), decide("Bash", "npm install", rules))
