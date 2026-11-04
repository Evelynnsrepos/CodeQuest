import math

PRICES = {"small": (0.25, 1.25), "big": (3.0, 15.0)}


def percentile(values, p):
    return 0


class Tracker:
    def __init__(self, prices=PRICES):
        self.prices = prices
        self.calls = []

    def record(self, model, tokens_in, tokens_out, ms):
        pass

    def cost(self):
        return 0.0

    def cost_by_model(self):
        return {}

    def latency(self):
        return {}

    def over_budget(self, limit):
        return False


t = Tracker()
for ms in [300, 320, 350, 400, 420, 450, 500, 600, 900, 4000]:
    t.record("small", 2000, 300, ms)
t.record("big", 10000, 1000, 2500)
print(round(t.cost(), 4), t.cost_by_model(), t.latency())
