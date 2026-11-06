def run_agent(model, tools, max_steps=5):
    # history = []
    # for step in range(max_steps):
    #     action = model(history)
    #     if "answer" in action: return action["answer"]
    #     tool = tools[action["tool"]]
    #     result = tool(action["args"])
    #     history.append((action["tool"], result))
    # after the loop: return "gave up"
    return ""


# A pretend model: first it asks for the weather tool, then it answers with the result.
def model(history):
    if len(history) == 0:
        return {"tool": "weather", "args": {"city": "Berlin"}}
    return {"answer": "It's " + history[-1][1] + " in Berlin."}


def weather(args):
    return "12 °C and rainy"


tools = {"weather": weather}
print(run_agent(model, tools))
