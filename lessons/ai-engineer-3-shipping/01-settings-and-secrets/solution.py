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
        return text.strip().lower() in ("1", "true", "yes", "on")
    return kind(text)


def load_settings(env, spec=SPEC):
    missing = sorted(name for name, (_, default) in spec.items() if default is REQUIRED and name not in env)
    if missing:
        raise ValueError("missing settings: " + ", ".join(missing))
    return {name: convert(kind, env[name]) if name in env else default for name, (kind, default) in spec.items()}


def safe_view(settings):
    secret = ("_KEY", "_TOKEN", "_PASSWORD")
    return {k: ("****" if k.endswith(secret) else v) for k, v in settings.items()}


s = load_settings({"OPENAI_API_KEY": "sk-secret", "TEMPERATURE": "0", "DEBUG": "yes"})
print(safe_view(s))
