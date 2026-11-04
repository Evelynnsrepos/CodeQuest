ha, fm, cd = ns.get("headless_args"), ns.get("field_matches"), ns.get("cron_due")
assert ha and fm and cd, "Keep headless_args, field_matches and cron_due."
want = ["claude", "-p", "Sum", "--output-format", "json", "--max-turns", "5", "--permission-mode", "dontAsk", "--allowedTools", "Read", "Glob"]
assert ha("Sum", ["Read", "Glob"], 5) == want, f"headless_args wrong: {ha('Sum', ['Read', 'Glob'], 5)!r}."
assert ha("Sum", ["Read"], 3, budget=0.5)[-4:] == ["--max-budget-usd", "0.5", "--allowedTools", "Read"], "Budget goes before --allowedTools."
assert fm("*", 13) and fm("30", 30) and not fm("30", 31), "* and plain numbers."
assert fm("1-5", 1) and fm("1-5", 5) and not fm("1-5", 6), "Ranges include both ends."
assert fm("*/15", 45) and not fm("*/15", 50), "Steps."
assert fm("0,30", 30) and not fm("0,30", 15) and fm("1-3,10", 10), "Comma lists."
assert cd("30 7 * * 1-5", 30, 7, 4, 11, 2) is True, "Tuesday 7:30 runs."
assert cd("30 7 * * 1-5", 30, 7, 8, 11, 6) is False, "Saturday doesn't."
assert cd("30 7 * * 1-5", 31, 7, 4, 11, 2) is False, "7:31 doesn't."
assert cd("*/15 * * * *", 45, 3, 1, 1, 0) is True, "Every 15 minutes."
