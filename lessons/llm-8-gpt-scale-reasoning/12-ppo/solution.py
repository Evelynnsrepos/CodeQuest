def ppo_objective(ratio, advantage, eps=0.2):
    clipped = ratio
    if clipped < 1 - eps:
        clipped = 1 - eps
    if clipped > 1 + eps:
        clipped = 1 + eps
    return min(ratio * advantage, clipped * advantage)


def kl_penalized_reward(reward, logp, logp_ref, beta):
    total = 0
    for i in range(len(logp)):
        total = total + logp[i] - logp_ref[i]
    return reward - beta * total


for ratio in [0.5, 0.9, 1.0, 1.1, 1.5]:
    print(f"ratio {ratio}: A=+1 -> {ppo_objective(ratio, 1.0):.2f}   A=-1 -> {ppo_objective(ratio, -1.0):.2f}")
print("reward with KL penalty:", round(kl_penalized_reward(2.0, [-1.0, -0.5, -2.0], [-1.2, -1.5, -2.0], 0.1), 3))
