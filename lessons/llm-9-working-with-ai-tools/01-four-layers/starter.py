LAYERS = {
    "model": ["qwen", "llama", "gemma", "claude", "mistral"],
    "runner": ["ollama", "llama.cpp", "lm studio", "vllm", "anthropic's api", "lemonade"],
    "harness": ["claude code", "open webui", "aider", "lm studio chat", "opencode", "goose", "continue"],
    "integration": ["mcp server", "tool", "skill", "hook", "subagent", "plugin", "slash command"],
}


def layer_of(name):
    # n = name.lower()
    # for layer in LAYERS:
    #     if n in LAYERS[layer]:
    #         return layer
    # return "unknown"
    return "unknown"


def pick_integration(need):
    # if need == "know how":
    #     return "skill"
    # if need == "be able":
    #     return "mcp"
    # if need == "always":
    #     return "hook"
    return None


print(layer_of("Ollama"), layer_of("claude code"), layer_of("hook"), pick_integration("always"))
