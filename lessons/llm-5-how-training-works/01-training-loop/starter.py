DATA = [(0.0, 1.1), (1.0, 3.9), (2.0, 7.2), (3.0, 9.8), (4.0, 13.1), (5.0, 16.0)]


def loss(w, b, data):
    return 0


def gradients(w, b, data):
    return 0, 0


def train(data, learning_rate, steps):
    w, b = 0.0, 0.0
    for step in range(steps):
        if step % 100 == 0:
            print(f"step {step:4}: loss {loss(w, b, data):.4f}")
    return w, b


w, b = train(DATA, 0.02, 500)
print(f"learned: y = {w:.2f}x + {b:.2f}")
