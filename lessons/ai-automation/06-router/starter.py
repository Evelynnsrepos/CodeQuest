def route(text, llm, handlers):
    return handlers["other"](text)


handlers = {
    "bill": lambda t: "saved to Bills",
    "newsletter": lambda t: "archived",
    "other": lambda t: "left for you",
}
print(route("Your electricity bill is ready", lambda p: "Bill.", handlers))
