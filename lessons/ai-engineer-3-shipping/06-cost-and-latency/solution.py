import math

PRICES = {"small": (0.25, 1.25), "big": (3.0, 15.0)}


def percentile(values, p):
    s = sorted(values)
    return s[max(1, math.ceil(p / 100 * len(s))) - 1]


class Tracker:
    def __init__(self, prices=PRICES):
        self.prices = prices
        self.calls = []

    def record(self, model, tokens_in, tokens_out, ms):
        pin, pout = self.prices[model]
        self.calls.append({"model": model, "ms": ms, "cost": (tokens_in * pin + tokens_out * pout) / 1_000_000})

    def cost(self):
        return sum(c["cost"] for c in self.calls)

    def cost_by_model(self):
        out = {}
        for c in self.calls:
            out[c["model"]] = out.get(c["model"], 0) + c["cost"]
        return out

    def latency(self):
        ms = [c["ms"] for c in self.calls]
        return {f"p{p}": percentile(ms, p) for p in (50, 95, 99)}

    def over_budget(self, limit):
        return self.cost() > limit


t = Tracker()
for ms in [300, 320, 350, 400, 420, 450, 500, 600, 900, 4000]:
    t.record("small", 2000, 300, ms)
t.record("big", 10000, 1000, 2500)
print(round(t.cost(), 4), t.cost_by_model(), t.latency())
