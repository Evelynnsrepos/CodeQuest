def accuracy(cases, replies):
    correct = 0
    for i in range(len(cases)):
        if cases[i]["expect"] == replies[i]["tool"]:
            correct = correct + 1
    return correct / len(cases)


def regressed(base_acc, tuned_acc, tolerance=0.05):
    return base_acc - tuned_acc > tolerance


cases = [
    {"expect": {"name": "get_weather", "args": {"city": "Berlin"}}},
    {"expect": {"name": "add", "args": {"a": 2, "b": 3}}},
    {"expect": None},
]
base = [{"tool": {"name": "get_weather", "args": {"city": "Berlin"}}},
        {"tool": {"name": "add", "args": {"a": 2, "b": 3}}},
        {"tool": None}]
tuned = [{"tool": {"name": "get_weather", "args": {"city": "berlin"}}},
         {"tool": {"name": "add", "args": {"a": 2, "b": 3}}},
         {"tool": None}]
b, t = accuracy(cases, base), accuracy(cases, tuned)
print("base", b, "tuned", t, "regressed:", regressed(b, t))
