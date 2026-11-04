def model_url(n8n_in_docker, model_in_compose, service, port):
    return f"http://localhost:{port}"


print(model_url(True, False, "lmstudio", 1234))
