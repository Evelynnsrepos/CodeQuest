def total_prob(p_b_given_a, p_a, p_b_given_not_a):
    return p_b_given_a * p_a + p_b_given_not_a * (1 - p_a)


def bayes(p_b_given_a, p_a, p_b_given_not_a):
    return p_b_given_a * p_a / total_prob(p_b_given_a, p_a, p_b_given_not_a)


print(total_prob(0.9, 0.01, 0.09), bayes(0.9, 0.01, 0.09))
