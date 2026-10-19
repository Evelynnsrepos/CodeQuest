assert "health" in ns, "There's no variable called health."
assert ns["health"] == 75, f"health should be 75, but it's {ns['health']!r}."
