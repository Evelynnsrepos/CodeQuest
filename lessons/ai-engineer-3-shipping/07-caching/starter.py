import hashlib
import json
import time


def cache_key(model, messages, temperature):
    return ""


class TTLCache:
    def __init__(self, ttl, max_items, now=time.monotonic):
        pass

    def get(self, key):
        return None

    def put(self, key, value):
        pass

    def hit_rate(self):
        return 0.0


def cached_call(cache, llm, model, messages, temperature):
    return llm(messages)


calls = []
llm = lambda msgs: calls.append(1) or f"answer #{len(calls)}"
cache = TTLCache(ttl=3600, max_items=100)
msgs = [{"role": "user", "content": "how do I reset my password?"}]
print([cached_call(cache, llm, "small", msgs, 0) for _ in range(3)], cache.hit_rate())
