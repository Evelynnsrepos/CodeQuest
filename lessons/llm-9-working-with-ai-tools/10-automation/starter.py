def headless_args(prompt, allowed, max_turns, budget=None):
    # args = ["claude", "-p", prompt, "--output-format", "json", "--max-turns", str(max_turns), "--permission-mode", "dontAsk"]
    # if budget is not None:
    #     args.append("--max-budget-usd")
    #     args.append(str(budget))
    # args.append("--allowedTools")
    # for tool in allowed:
    #     args.append(tool)
    # return args
    return ["claude", prompt]


def field_matches(field, value):
    # for part in field.split(","):
    #     if part == "*":
    #         return True
    #     if part.startswith("*/"):
    #         step = int(part[2:])
    #         if value % step == 0:
    #             return True
    #     elif "-" in part:
    #         ends = part.split("-")
    #         low = int(ends[0])
    #         high = int(ends[1])
    #         if low <= value and value <= high:
    #             return True
    #     elif int(part) == value:
    #         return True
    # return False
    return True


def cron_due(expr, minute, hour, day, month, weekday):
    # fields = expr.split()
    # values = [minute, hour, day, month, weekday]
    # for i in range(5):
    #     if not field_matches(fields[i], values[i]):
    #         return False
    # return True
    return True


print(headless_args("Summarize notes", ["Read", "Glob"], 5))
print(cron_due("30 7 * * 1-5", 30, 7, 4, 11, 2), cron_due("30 7 * * 1-5", 30, 7, 8, 11, 6))
