def headless_args(prompt, allowed, max_turns, budget=None):
    args = ["claude", "-p", prompt, "--output-format", "json", "--max-turns", str(max_turns), "--permission-mode", "dontAsk"]
    if budget is not None:
        args += ["--max-budget-usd", str(budget)]
    return args + ["--allowedTools", *allowed]


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
    fields = expr.split()
    return all(field_matches(f, v) for f, v in zip(fields, (minute, hour, day, month, weekday)))


print(headless_args("Summarize notes", ["Read", "Glob"], 5))
print(cron_due("30 7 * * 1-5", 30, 7, 4, 11, 2), cron_due("30 7 * * 1-5", 30, 7, 8, 11, 6))
