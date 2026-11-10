def model_url(n8n_in_docker, model_in_compose, service, port):
    if n8n_in_docker == False:
        host = "localhost"
    elif model_in_compose:
        host = service
    else:
        host = "host.docker.internal"
    return "http://" + host + ":" + str(port)


print(model_url(True, False, "lmstudio", 1234))
