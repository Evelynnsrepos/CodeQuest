import math

PRICES = {"small": (0.25, 1.25), "big": (3.0, 15.0)}


def percentile(values, p):
    # s = sorted(values)
    # rank = math.ceil(p / 100 * len(s))
    # if rank < 1:
    #     rank = 1
    # return s[rank - 1]
    return 0


class Tracker:
    def __init__(self, prices=PRICES):
        self.prices = prices
        self.calls = []

    def record(self, model, tokens_in, tokens_out, ms):
        # price_in, price_out = self.prices[model]
        # cost = (tokens_in * price_in + tokens_out * price_out) / 1_000_000
        # self.calls.append({"model": model, "ms": ms, "cost": cost})
        pass

    def cost(self):
        # total = 0.0
        # for c in self.calls:
        #     total = total + c["cost"]
        # return total
        return 0.0

    def cost_by_model(self):
        # out = {}
        # for c in self.calls:
        #     out[c["model"]] = out.get(c["model"], 0) + c["cost"]
        # return out
        return {}

    def latency(self):
        # ms = []
        # for c in self.calls:
        #     ms.append(c["ms"])
        # return {"p50": percentile(ms, 50), "p95": percentile(ms, 95), "p99": percentile(ms, 99)}
        return {}

    def over_budget(self, limit):
        # return self.cost() > limit
        return False


t = Tracker()
for ms in [300, 320, 350, 400, 420, 450, 500, 600, 900, 4000]:
    t.record("small", 2000, 300, ms)
t.record("big", 10000, 1000, 2500)
print(round(t.cost(), 4), t.cost_by_model(), t.latency())
