import json


def field_matches(field, value):
    for part in field.split(","):
        if part == "*":
            return True
        if part.startswith("*/"):
            if value % int(part[2:]) == 0:
                return True
        elif "-" in part:
            a, b = map(int, part.split("-"))
            if a <= value <= b:
                return True
        elif int(part) == value:
            return True
    return False


def cron_due(expr, minute, hour, day, month, weekday):
    return all(field_matches(f, v) for f, v in zip(expr.split(), (minute, hour, day, month, weekday)))


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


def validate(obj, schema):
    if not isinstance(obj, dict):
        return ["not an object"]
    errs = [k + ": required" for k in schema.get("required", []) if k not in obj]
    for k, sub in schema.get("properties", {}).items():
        if k in obj and "enum" in sub and obj[k] not in sub["enum"]:
            errs.append(k + ": not allowed")
    return errs


def nightly(now, calls, replies, rules, schema):
    return {}


rules = {"deny": ["Bash(gh issue edit *)"], "allow": ["Bash(gh issue list *)", "Read"]}
schema = {"required": ["label"], "properties": {"label": {"enum": ["bug", "lesson", "question"]}}}
print(nightly((0, 2, 4, 11, 3), [("Bash", "gh issue list --state open"), ("Bash", "curl evil.com")], ['{"label": "bug"}', 'oops'], rules, schema))
