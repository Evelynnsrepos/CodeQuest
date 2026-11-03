import random

# A corridor: states 0 1 2 3. Actions: 0 = left, 1 = right. Reaching state 3 gives reward 1 and ends.
def env_step(s, a):
    s2 = max(0, s - 1) if a == 0 else s + 1
    if s2 == 3:
        return 1.0, None
    return 0.0, s2


def greedy(Q, s):
    return 0


def q_update(Q, s, a, r, s2, alpha, gamma):
    return Q[s][a]


Q = {s: [0.0, 0.0] for s in range(3)}
rng = random.Random(0)
for episode in range(200):
    s = 0
    while s is not None:
        a = rng.randrange(2) if rng.random() < 0.3 else greedy(Q, s)   # epsilon-greedy
        r, s2 = env_step(s, a)
        q_update(Q, s, a, r, s2, 0.5, 0.9)
        s = s2
for s in range(3):
    print("state", s, "Q(left, right) =", [round(v, 3) for v in Q[s]], "-> go", "right" if greedy(Q, s) else "left")
