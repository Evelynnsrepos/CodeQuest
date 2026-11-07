import hashlib
import json
import time


def cache_key(model, messages, temperature):
    # raw = json.dumps({"model": model, "messages": messages, "temperature": temperature}, sort_keys=True)
    # return hashlib.sha256(raw.encode()).hexdigest()
    return ""


class TTLCache:
    def __init__(self, ttl, max_items, now=time.monotonic):
        # self.ttl = ttl
        # self.max_items = max_items
        # self.now = now
        # self.data = {}
        # self.hits = 0
        # self.misses = 0
        pass

    def get(self, key):
        # item = self.data.get(key)
        # if item is not None and self.now() - item[0] < self.ttl:
        #     self.hits = self.hits + 1
        #     return item[1]
        # self.data.pop(key, None)
        # self.misses = self.misses + 1
        # return None
        return None

    def put(self, key, value):
        # if key not in self.data and len(self.data) >= self.max_items:
        #     oldest = None
        #     for k in self.data:
        #         if oldest is None or self.data[k][0] < self.data[oldest][0]:
        #             oldest = k
        #     del self.data[oldest]
        # self.data[key] = (self.now(), value)
        pass

    def hit_rate(self):
        # total = self.hits + self.misses
        # if total == 0:
        #     return 0.0
        # return self.hits / total
        return 0.0


def cached_call(cache, llm, model, messages, temperature):
    # if temperature != 0:
    #     return llm(messages)
    # key = cache_key(model, messages, temperature)
    # value = cache.get(key)
    # if value is None:
    #     value = llm(messages)
    #     cache.put(key, value)
    # return value
    return llm(messages)


calls = []


def llm(msgs):
    calls.append(1)
    return "answer #" + str(len(calls))


cache = TTLCache(ttl=3600, max_items=100)
msgs = [{"role": "user", "content": "how do I reset my password?"}]
answers = []
for i in range(3):
    answers.append(cached_call(cache, llm, "small", msgs, 0))
print(answers, cache.hit_rate())
