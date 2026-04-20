from scipy.stats import binom

n = 10   # 10 trials
p = 0.9  # 90% success rate assumed

# What's the probability of getting exactly 8 successes?
print(f"P(k=8) = {binom.pmf(8, n, p):.4f}")   # 0.1937

# What's the probability of 8 OR FEWER successes?
print(f"P(k<=8) = {binom.cdf(8, n, p):.4f}")  # 0.2639

# The book's insight: even if true rate is 90%,
# there's a 26% chance you only see 8/10 successes
# → small samples are deceiving → need more data