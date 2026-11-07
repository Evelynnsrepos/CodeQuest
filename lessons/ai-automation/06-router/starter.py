def route(text, llm, handlers):
    # labels = list(handlers)
    # prompt = "Answer with one word from: " + ", ".join(labels) + ".\n\n" + text
    # reply = llm(prompt).strip().lower().strip(".")
    # handler = handlers.get(reply, handlers["other"])
    # return handler(text)
    return handlers["other"](text)


def save_bill(text):
    return "saved to Bills"


def archive(text):
    return "archived"


def leave_for_me(text):
    return "left for you"


def fake_llm(prompt):
    return "Bill."


handlers = {"bill": save_bill, "newsletter": archive, "other": leave_for_me}
print(route("Your electricity bill is ready", fake_llm, handlers))
