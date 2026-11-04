def expected(d):
    return sum(x * p for x, p in d.items())


def expected_f(d, f):
    return sum(f(x) * p for x, p in d.items())


def expected_reward(policy, rewards):
    return sum(p * rewards[y] for y, p in policy.items())


die = {k: 1 / 6 for k in range(1, 7)}
print(expected(die), expected_f(die, lambda x: x * x), expected_reward({"a": 0.7, "b": 0.3}, {"a": 1, "b": 0}))
