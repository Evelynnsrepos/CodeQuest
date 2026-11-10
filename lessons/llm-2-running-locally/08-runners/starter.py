PORTS = {
    "lmstudio": 0,
    "ollama": 0,
    "llamacpp": 0,
}


def base_url(runner):
    # port = PORTS[runner]
    # return "http://localhost:" + str(port) + "/v1"
    return ""


for runner in PORTS:
    print(runner, base_url(runner))
