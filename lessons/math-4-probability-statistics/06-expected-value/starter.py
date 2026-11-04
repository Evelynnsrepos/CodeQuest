def expected(d):
    return 0


def expected_f(d, f):
    return 0


def expected_reward(policy, rewards):
    return 0


die = {k: 1 / 6 for k in range(1, 7)}
print(expected(die), expected_f(die, lambda x: x * x), expected_reward({"a": 0.7, "b": 0.3}, {"a": 1, "b": 0}))
