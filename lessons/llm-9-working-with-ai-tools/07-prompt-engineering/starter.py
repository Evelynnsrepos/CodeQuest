def build_prompt(task, why, documents, examples, fmt):
    return task


print(build_prompt("Summarize the bug report in 3 bullets.", "It is a phone notification.", ["App crashes on start"], [("x", "y")], "Answer with only the bullets."))
