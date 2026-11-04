def label_for(text, llm, labels):
    return llm(text)


def fake_llm(prompt):
    return "  Spam.\n"


print(label_for("You won a free cruise!!!", fake_llm, ["work", "private", "spam"]))
