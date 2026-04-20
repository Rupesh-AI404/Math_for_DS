from scipy.stats import beta

# You ran 10 engine tests: 8 successes, 2 failures
# What is the ACTUAL underlying success rate?
a, b = 8, 2   # alpha = successes, beta = failures

# Probability the true rate is >= 90%
p_above_90 = 1 - beta.cdf(0.90, a, b)
print(f"P(true rate >= 90%) = {p_above_90:.3f}")   # 0.225 → only 22.5%!

# After 30 successes, 6 failures (more data = more certainty)
a2, b2 = 30, 6
p_above_90_more_data = 1 - beta.cdf(0.90, a2, b2)
print(f"P(true rate >= 90%) with more data = {p_above_90_more_data:.3f}")  # 0.131

# Distribution narrows as you get more data — uncertainty shrinks
# Used in Bayesian A/B testing and bandit algorithms