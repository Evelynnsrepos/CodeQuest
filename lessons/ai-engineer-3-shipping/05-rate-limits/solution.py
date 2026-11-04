import time


class TokenBucket:
    def __init__(self, rate, capacity, now=time.monotonic):
        self.rate, self.capacity, self.now = rate, capacity, now
        self.tokens = float(capacity)
        self.last = now()

    def _refill(self):
        t = self.now()
        self.tokens = min(self.capacity, self.tokens + (t - self.last) * self.rate)
        self.last = t

    def allow(self):
        self._refill()
        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False

    def retry_after(self):
        self._refill()
        return 0.0 if self.tokens >= 1 else (1 - self.tokens) / self.rate


class Limiter:
    def __init__(self, rate, capacity, now=time.monotonic):
        self.rate, self.capacity, self.now = rate, capacity, now
        self.buckets = {}

    def check(self, key):
        if key not in self.buckets:
            self.buckets[key] = TokenBucket(self.rate, self.capacity, self.now)
        b = self.buckets[key]
        ok = b.allow()
        return ok, 0.0 if ok else b.retry_after()


t = [0.0]
b = TokenBucket(rate=1, capacity=3, now=lambda: t[0])
print([b.allow() for _ in range(5)], b.retry_after())
t[0] = 2.0
print(b.allow(), b.allow(), b.allow())
