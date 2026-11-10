REQUIRED = object()
SPEC = {
    "MODEL": (str, "llama3.2"),
    "BASE_URL": (str, "http://localhost:11434/v1"),
    "TEMPERATURE": (float, 0.2),
    "MAX_TOKENS": (int, 512),
    "DEBUG": (bool, False),
    "OPENAI_API_KEY": (str, REQUIRED),
}


def convert(kind, text):
    if kind is bool:
        return text.strip().lower() in ["1", "true", "yes", "on"]
    return kind(text)


def load_settings(env, spec=SPEC):
    missing = []
    for name in spec:
        kind, default = spec[name]
        if default is REQUIRED and name not in env:
            missing.append(name)
    if len(missing) > 0:
        raise ValueError("missing settings: " + ", ".join(sorted(missing)))
    out = {}
    for name in spec:
        kind, default = spec[name]
        if name in env:
            out[name] = convert(kind, env[name])
        else:
            out[name] = default
    return out


def safe_view(settings):
    out = {}
    for k in settings:
        if k.endswith("_KEY") or k.endswith("_TOKEN") or k.endswith("_PASSWORD"):
            out[k] = "****"
        else:
            out[k] = settings[k]
    return out


s = load_settings({"OPENAI_API_KEY": "sk-secret", "TEMPERATURE": "0", "DEBUG": "yes"})
print(safe_view(s))
