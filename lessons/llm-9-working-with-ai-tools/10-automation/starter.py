def headless_args(prompt, allowed, max_turns, budget=None):
    return ["claude", prompt]


def field_matches(field, value):
    return True


def cron_due(expr, minute, hour, day, month, weekday):
    return True


print(headless_args("Summarize notes", ["Read", "Glob"], 5))
print(cron_due("30 7 * * 1-5", 30, 7, 4, 11, 2), cron_due("30 7 * * 1-5", 30, 7, 8, 11, 6))
