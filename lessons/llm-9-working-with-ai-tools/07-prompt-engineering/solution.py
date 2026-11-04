def build_prompt(task, why, documents, examples, fmt):
    parts = ["<documents>"]
    parts += ['<document index="%d">%s</document>' % (i, d) for i, d in enumerate(documents, 1)]
    parts.append("</documents>")
    if examples:
        parts.append("<examples>")
        parts += ["<example><input>%s</input><output>%s</output></example>" % ex for ex in examples]
        parts.append("</examples>")
    parts.append("<instructions>" + task + " " + why + "</instructions>")
    parts.append(fmt)
    return "\n".join(parts)


print(build_prompt("Summarize the bug report in 3 bullets.", "It is a phone notification.", ["App crashes on start"], [("x", "y")], "Answer with only the bullets."))
