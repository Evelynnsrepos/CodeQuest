PORTS = {
    "lmstudio": 1234,
    "ollama": 11434,
    "llamacpp": 8080,
}


def base_url(runner):
    port = PORTS[runner]
    return f"http://localhost:{port}/v1"


for runner in PORTS:
    print(runner, "→", base_url(runner))
