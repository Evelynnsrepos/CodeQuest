import math


def implicit_reward(logp_policy, logp_ref, beta):
    return beta * (logp_policy - logp_ref)


def dpo_loss(pc, pr, rc, rr, beta):
    margin = implicit_reward(pc, rc, beta) - implicit_reward(pr, rr, beta)
    return math.log(1 + math.exp(-margin))


def reward_accuracy(batch, beta):
    wins = 0
    for pc, pr, rc, rr in batch:
        if implicit_reward(pc, rc, beta) > implicit_reward(pr, rr, beta):
            wins += 1
    return wins / len(batch)


# summed log-probs of whole answers (very negative: they're products of many token probabilities)
start = (-42.0, -40.0, -42.0, -40.0)        # policy == reference: nothing learned yet
later = (-38.0, -47.0, -42.0, -40.0)        # chosen got likelier, rejected less likely
print("loss at start:", round(dpo_loss(*start, 0.1), 4), "(log 2 =", round(math.log(2), 4), ")")
print("loss later:   ", round(dpo_loss(*later, 0.1), 4))
print("reward accuracy:", reward_accuracy([start, later, (-50.0, -45.0, -42.0, -40.0)], 0.1))
