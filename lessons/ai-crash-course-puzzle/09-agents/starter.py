def run_agent(model, tools, max_steps=5):
    history = []
    for step in range(max_steps):
        ___
        if "answer" in action:
            ___
        ___
        ___
        ___
    return "gave up"


# A pretend model: first it asks for the weather tool, then it answers with the result.
def model(history):
    if len(history) == 0:
        return {"tool": "weather", "args": {"city": "Berlin"}}
    return {"answer": "It's " + history[-1][1] + " in Berlin."}


def weather(args):
    return "12 °C and rainy"


tools = {"weather": weather}
print(run_agent(model, tools))
