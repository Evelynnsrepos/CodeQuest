LAYERS = {
    "model": ["qwen", "llama", "gemma", "claude", "mistral"],
    "runner": ["ollama", "llama.cpp", "lm studio", "vllm", "anthropic's api", "lemonade"],
    "harness": ["claude code", "open webui", "aider", "lm studio chat", "opencode", "goose", "continue"],
    "integration": ["mcp server", "tool", "skill", "hook", "subagent", "plugin", "slash command"],
}


def layer_of(name):
    n = name.lower()
    for layer, names in LAYERS.items():
        if n in names:
            return layer
    return "unknown"


def pick_integration(need):
    return {"know how": "skill", "be able": "mcp", "always": "hook"}[need]


print(layer_of("Ollama"), layer_of("claude code"), layer_of("hook"), pick_integration("always"))
