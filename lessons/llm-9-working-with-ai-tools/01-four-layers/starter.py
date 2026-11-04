LAYERS = {}


def layer_of(name):
    return "unknown"


def pick_integration(need):
    return None


print(layer_of("Ollama"), layer_of("claude code"), layer_of("hook"), pick_integration("always"))
