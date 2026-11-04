import hashlib
import json
import time


def cache_key(model, messages, temperature):
    raw = json.dumps({"model": model, "messages": messages, "temperature": temperature}, sort_keys=True)
    return hashlib.sha256(raw.encode()).hexdigest()


class TTLCache:
    def __init__(self, ttl, max_items, now=time.monotonic):
        self.ttl, self.max_items, self.now = ttl, max_items, now
        self.data = {}
        self.hits = self.misses = 0

    def get(self, key):
        item = self.data.get(key)
        if item and self.now() - item[0] < self.ttl:
            self.hits += 1
            return item[1]
        self.data.pop(key, None)
        self.misses += 1
        return None

    def put(self, key, value):
        if key not in self.data and len(self.data) >= self.max_items:
            oldest = min(self.data, key=lambda k: self.data[k][0])
            del self.data[oldest]
        self.data[key] = (self.now(), value)

    def hit_rate(self):
        total = self.hits + self.misses
        return self.hits / total if total else 0.0


def cached_call(cache, llm, model, messages, temperature):
    if temperature != 0:
        return llm(messages)
    key = cache_key(model, messages, temperature)
    value = cache.get(key)
    if value is None:
        value = llm(messages)
        cache.put(key, value)
    return value


calls = []
llm = lambda msgs: calls.append(1) or f"answer #{len(calls)}"
cache = TTLCache(ttl=3600, max_items=100)
msgs = [{"role": "user", "content": "how do I reset my password?"}]
print([cached_call(cache, llm, "small", msgs, 0) for _ in range(3)], cache.hit_rate())
