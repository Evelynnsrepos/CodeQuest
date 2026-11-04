def route(text, llm, handlers):
    labels = list(handlers)
    prompt = f"Answer with one word from: {', '.join(labels)}.\n\n{text}"
    reply = llm(prompt).strip().lower().strip(".")
    handler = handlers.get(reply, handlers["other"])
    return handler(text)


handlers = {
    "bill": lambda t: "saved to Bills",
    "newsletter": lambda t: "archived",
    "other": lambda t: "left for you",
}
print(route("Your electricity bill is ready", lambda p: "Bill.", handlers))
