REQUIRED = object()
SPEC = {
    "MODEL": (str, "llama3.2"),
    "BASE_URL": (str, "http://localhost:11434/v1"),
    "TEMPERATURE": (float, 0.2),
    "MAX_TOKENS": (int, 512),
    "DEBUG": (bool, False),
    "OPENAI_API_KEY": (str, REQUIRED),
}


def load_settings(env, spec=SPEC):
    return {}


def safe_view(settings):
    return settings


s = load_settings({"OPENAI_API_KEY": "sk-secret", "TEMPERATURE": "0", "DEBUG": "yes"})
print(safe_view(s))
