def build_prompt(task, why, documents, examples, fmt):
    parts = ["<documents>"]
    i = 1
    for doc in documents:
        parts.append('<document index="' + str(i) + '">' + doc + "</document>")
        i = i + 1
    parts.append("</documents>")
    if len(examples) > 0:
        parts.append("<examples>")
        for inp, out in examples:
            parts.append("<example><input>" + inp + "</input><output>" + out + "</output></example>")
        parts.append("</examples>")
    parts.append("<instructions>" + task + " " + why + "</instructions>")
    parts.append(fmt)
    return "\n".join(parts)


print(build_prompt("Summarize the bug report in 3 bullets.", "It is a phone notification.", ["App crashes on start"], [("x", "y")], "Answer with only the bullets."))
