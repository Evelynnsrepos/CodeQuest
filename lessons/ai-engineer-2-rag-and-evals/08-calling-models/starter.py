import time
import httpx


def chat(messages, model, base, client, retries=3, sleep=time.sleep):
    return "", {}


# Try it against a real local model (Ollama must be running):
# with httpx.Client() as c:
#     print(chat([{"role": "user", "content": "Say hi in German"}], "llama3.2", "http://localhost:11434/v1", c))
print(chat.__doc__)
