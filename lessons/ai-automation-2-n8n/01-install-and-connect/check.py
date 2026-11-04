f = ns.get("model_url")
assert f, "Define a function called model_url."
assert f(False, False, "ollama", 11434) == "http://localhost:11434", "n8n not in Docker: localhost."
assert f(True, True, "ollama", 11434) == "http://ollama:11434", "Same compose file: use the service name."
assert f(True, False, "lmstudio", 1234) == "http://host.docker.internal:1234", "n8n in Docker, model on your computer: host.docker.internal."
assert f(False, True, "ollama", 11434) == "http://localhost:11434", "If n8n isn't in Docker, it's localhost either way."
