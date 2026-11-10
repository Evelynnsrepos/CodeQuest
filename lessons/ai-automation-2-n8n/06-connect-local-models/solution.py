def setup_problems(cfg):
    url = cfg["base_url"].rstrip("/")
    problems = []
    if url.endswith("/chat/completions"):
        problems.append("cut the URL at /v1")
    elif url.endswith("/v1") == False:
        problems.append("add /v1 to the URL")
    if cfg["n8n_in_docker"] and ("localhost" in url or "127.0.0.1" in url):
        problems.append("use host.docker.internal")
    if cfg["use_responses_api"]:
        problems.append("turn off Use Responses API")
    if cfg["model"] == "":
        problems.append("set the model ID")
    return problems


print(setup_problems({"base_url": "http://localhost:1234/v1/chat/completions", "n8n_in_docker": True, "use_responses_api": True, "model": ""}))
