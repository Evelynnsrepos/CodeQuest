import math


def route(scores, k):
    # top = []
    # for step in range(k):
    #     best = None
    #     for i in range(len(scores)):
    #         if i not in top:
    #             if best is None or scores[i] > scores[best]:
    #                 best = i
    #     top.append(best)
    # m = scores[top[0]]
    # es = []
    # total = 0
    # for i in top:
    #     e = math.exp(scores[i] - m)
    #     es.append(e)
    #     total = total + e
    # out = []
    # for j in range(len(top)):
    #     out.append((top[j], es[j] / total))
    # return out
    return []


def moe_output(scores, k, expert_outputs):
    # out = [0.0] * len(expert_outputs[0])
    # for i, g in route(scores, k):
    #     for j in range(len(out)):
    #         out[j] = out[j] + g * expert_outputs[i][j]
    # return out
    return []


def balance_loss(f, P, alpha=1.0):
    # total = 0
    # for i in range(len(f)):
    #     total = total + f[i] * P[i]
    # return alpha * len(f) * total
    return 0


print(route([2, 1, 0.5, -1], 2), round(balance_loss([0.5, 0.3, 0.1, 0.1], [0.4, 0.3, 0.2, 0.1]), 4))
