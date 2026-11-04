import time


class TokenBucket:
    def __init__(self, rate, capacity, now=time.monotonic):
        pass

    def allow(self):
        return True

    def retry_after(self):
        return 0.0


class Limiter:
    def __init__(self, rate, capacity, now=time.monotonic):
        pass

    def check(self, key):
        return True, 0.0


t = [0.0]
b = TokenBucket(rate=1, capacity=3, now=lambda: t[0])
print([b.allow() for _ in range(5)], b.retry_after())
t[0] = 2.0
print(b.allow(), b.allow(), b.allow())
