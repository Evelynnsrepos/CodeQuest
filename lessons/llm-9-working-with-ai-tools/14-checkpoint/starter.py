import json


def field_matches(field, value):
    for part in field.split(","):
        if part == "*":
            return True
        if part.startswith("*/"):
            step = int(part[2:])
            if value % step == 0:
                return True
        elif "-" in part:
            ends = part.split("-")
            low = int(ends[0])
            high = int(ends[1])
            if low <= value and value <= high:
                return True
        elif int(part) == value:
            return True
    return False


def cron_due(expr, minute, hour, day, month, weekday):
    fields = expr.split()
    values = [minute, hour, day, month, weekday]
    for i in range(5):
        if not field_matches(fields[i], values[i]):
            return False
    return True


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


def validate(obj, schema):
    if not isinstance(obj, dict):
        return ["not an object"]
    errs = []
    for k in schema.get("required", []):
        if k not in obj:
            errs.append(k + ": required")
    properties = schema.get("properties", {})
    for k in properties:
        sub = properties[k]
        if k in obj and "enum" in sub and obj[k] not in sub["enum"]:
            errs.append(k + ": not allowed")
    return errs


def nightly(now, calls, replies, rules, schema):
    # if not cron_due("0 2 * * *", now[0], now[1], now[2], now[3], now[4]):
    #     return None
    # ran = []
    # blocked = []
    # for call in calls:
    #     if decide(call[0], call[1], rules) == "allow":
    #         ran.append(call)
    #     else:
    #         blocked.append(call)
    # labels = []
    # for raw in replies:
    #     try:
    #         obj = json.loads(raw)
    #     except json.JSONDecodeError:
    #         continue
    #     if validate(obj, schema) == []:
    #         labels.append(obj["label"])
    # return {"ran": ran, "blocked": blocked, "labels": labels}
    return {}


rules = {"deny": ["Bash(gh issue edit *)"], "allow": ["Bash(gh issue list *)", "Read"]}
schema = {"required": ["label"], "properties": {"label": {"enum": ["bug", "lesson", "question"]}}}
print(nightly((0, 2, 4, 11, 3), [("Bash", "gh issue list --state open"), ("Bash", "curl evil.com")], ['{"label": "bug"}', 'oops'], rules, schema))
