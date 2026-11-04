def model_url(n8n_in_docker, model_in_compose, service, port):
    if not n8n_in_docker:
        host = "localhost"
    elif model_in_compose:
        host = service
    else:
        host = "host.docker.internal"
    return f"http://{host}:{port}"


print(model_url(True, False, "lmstudio", 1234))
