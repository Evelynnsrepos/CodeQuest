def label_for(text, llm, labels):
    prompt = f"Answer with one word from: {', '.join(labels)}.\n\n{text}"
    reply = llm(prompt).strip().lower().strip(".")
    return reply if reply in labels else "other"


def fake_llm(prompt):
    return "  Spam.\n"


print(label_for("You won a free cruise!!!", fake_llm, ["work", "private", "spam"]))
