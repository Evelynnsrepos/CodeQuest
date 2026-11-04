f = ns.get("label_for")
assert f, "Define a function called label_for."
labels = ["work", "private", "spam"]
seen = []
def spy(prompt):
    seen.append(prompt)
    return "Work."
assert f("Meeting at 10", spy, labels) == "work", "Clean 'Work.' into 'work'."
assert len(seen) == 1, f"Call llm exactly once, not {len(seen)} times."
assert "Meeting at 10" in seen[0], "Put the text in the prompt."
assert "work, private, spam" in seen[0], "List the labels in the prompt, joined with ', '."
assert f("x", lambda p: "  PRIVATE\n", labels) == "private", "Strip spaces and newlines, make it lowercase."
assert f("x", lambda p: "I think it is spam because...", labels) == "other", "Anything not exactly a label becomes 'other'."
assert f("x", lambda p: "", labels) == "other", "An empty reply becomes 'other'."
