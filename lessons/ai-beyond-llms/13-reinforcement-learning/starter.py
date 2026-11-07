import random

# A corridor: states 0 1 2 3. Actions: 0 = left, 1 = right. Reaching state 3 gives reward 1 and ends.
def env_step(s, a):
    if a == 0:
        s2 = max(0, s - 1)
    else:
        s2 = s + 1
    if s2 == 3:
        return 1.0, None
    return 0.0, s2


def greedy(Q, s):
    # values = Q[s]
    # best = 0
    # for a in range(len(values)):
    #     if values[a] > values[best]:
    #         best = a
    # return best
    return 0


def q_update(Q, s, a, r, s2, alpha, gamma):
    # if s2 is None:
    #     target = r
    # else:
    #     target = r + gamma * max(Q[s2])
    # Q[s][a] = Q[s][a] + alpha * (target - Q[s][a])
    # return Q[s][a]
    return Q[s][a]


Q = {0: [0.0, 0.0], 1: [0.0, 0.0], 2: [0.0, 0.0]}
rng = random.Random(0)
for episode in range(200):
    s = 0
    while s is not None:
        if rng.random() < 0.3:   # epsilon-greedy: sometimes a random action
            a = rng.randrange(2)
        else:
            a = greedy(Q, s)
        r, s2 = env_step(s, a)
        q_update(Q, s, a, r, s2, 0.5, 0.9)
        s = s2
for s in range(3):
    print("state", s, "Q(left, right) =", [round(v, 3) for v in Q[s]], "-> go", ["left", "right"][greedy(Q, s)])
