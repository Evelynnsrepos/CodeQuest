import time


class TokenBucket:
    def __init__(self, rate, capacity, now=time.monotonic):
        self.rate = rate
        self.capacity = capacity
        self.now = now
        self.tokens = float(capacity)
        self.last = now()

    def _refill(self):
        t = self.now()
        self.tokens = min(self.capacity, self.tokens + (t - self.last) * self.rate)
        self.last = t

    def allow(self):
        self._refill()
        if self.tokens >= 1:
            self.tokens = self.tokens - 1
            return True
        return False

    def retry_after(self):
        self._refill()
        if self.tokens >= 1:
            return 0.0
        return (1 - self.tokens) / self.rate


class Limiter:
    def __init__(self, rate, capacity, now=time.monotonic):
        self.rate = rate
        self.capacity = capacity
        self.now = now
        self.buckets = {}

    def check(self, key):
        if key not in self.buckets:
            self.buckets[key] = TokenBucket(self.rate, self.capacity, self.now)
        b = self.buckets[key]
        if b.allow():
            return True, 0.0
        return False, b.retry_after()


t = [0.0]


def fake_clock():
    return t[0]


b = TokenBucket(rate=1, capacity=3, now=fake_clock)
results = []
for i in range(5):
    results.append(b.allow())
print(results, b.retry_after())
t[0] = 2.0
print(b.allow(), b.allow(), b.allow())
