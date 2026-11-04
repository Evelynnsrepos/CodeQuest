import time
import httpx


def chat(messages, model, base, client, retries=3, sleep=time.sleep):
    wait = 1.0
    for attempt in range(retries + 1):
        try:
            r = client.post(f"{base}/chat/completions", timeout=60,
                            json={"model": model, "messages": messages, "temperature": 0})
        except httpx.TimeoutException:
            r = None
        if r is not None and r.status_code != 429 and r.status_code < 500:
            r.raise_for_status()
            data = r.json()
            return data["choices"][0]["message"]["content"], data.get("usage", {})
        if attempt == retries:
            break
        delay = float(r.headers["Retry-After"]) if r is not None and "Retry-After" in r.headers else wait
        sleep(delay)
        wait *= 2
    raise RuntimeError("model unavailable")


# Try it against a real local model (Ollama must be running):
# with httpx.Client() as c:
#     print(chat([{"role": "user", "content": "Say hi in German"}], "llama3.2", "http://localhost:11434/v1", c))
print(chat.__doc__)
