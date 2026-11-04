def run_agent(model, tools, max_steps=5):
    history = []
    for _ in range(max_steps):
        action = model(history)
        if "answer" in action:
            return action["answer"]
        result = tools[action["tool"]](**action["args"])
        history.append((action["tool"], result))
    return "gave up"


def model(history):
    if not history:
        return {"tool": "weather", "args": {"city": "Berlin"}}
    return {"answer": f"It's {history[-1][1]} in Berlin."}


tools = {"weather": lambda city: "12 °C and rainy"}
print(run_agent(model, tools))
