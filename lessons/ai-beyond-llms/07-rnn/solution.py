import math


def matvec(W, x):
    return [sum(w * v for w, v in zip(row, x)) for row in W]


def rnn_step(x, h, Wx, Wh, b):
    return [math.tanh(a + c + d) for a, c, d in zip(matvec(Wx, x), matvec(Wh, h), b)]


def run_rnn(xs, Wx, Wh, b):
    h = [0.0] * len(b)
    states = []
    for x in xs:
        h = rnn_step(x, h, Wx, Wh, b)
        states.append(h)
    return states


Wx = [[0.5], [-0.3]]          # 1 input -> 2 hidden
Wh = [[0.8, 0.0], [0.2, 0.9]]
b = [0.0, 0.1]
states = run_rnn([[1.0], [0.0], [0.0], [0.0]], Wx, Wh, b)
for t, h in enumerate(states):
    print(t, [round(v, 3) for v in h])
print("gradient after 50 steps with factor 0.9:", round(0.9 ** 50, 5))
