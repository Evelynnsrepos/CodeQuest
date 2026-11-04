import math


def train_flops(N, D):
    return 6 * N * D


def chinchilla_optimal(C):
    N = math.sqrt(C / 120)
    return (N, 20 * N)


def predicted_loss(N, D):
    return 1.69 + 406.4 / N ** 0.34 + 410.7 / D ** 0.28


C = 1e21
N, D = chinchilla_optimal(C)
print(f"budget {C:.0e} FLOPs -> {N/1e9:.1f}B params on {D/1e9:.0f}B tokens, check {train_flops(N, D):.2e}")
print("predicted loss:", round(predicted_loss(N, D), 3))
print("same budget, 10x bigger model:", round(predicted_loss(10 * N, D / 10), 3))
