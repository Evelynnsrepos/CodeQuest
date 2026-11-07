def label_for(text, llm, labels):
    prompt = "Answer with one word from: " + ", ".join(labels) + ".\n\n" + text
    reply = llm(prompt).strip().lower().strip(".")
    if reply in labels:
        return reply
    return "other"


def fake_llm(prompt):
    return "  Spam.\n"


print(label_for("You won a free cruise!!!", fake_llm, ["work", "private", "spam"]))
