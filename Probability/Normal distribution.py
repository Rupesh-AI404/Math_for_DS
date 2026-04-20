from scipy.stats import norm
import numpy as np

mean, std = 0, 1   # standard normal

# Three questions you need to answer fluently:

# Q1: What's the probability of x < 1.96?
print(f"P(x < 1.96) = {norm.cdf(1.96, mean, std):.3f}")   # 0.975

# Q2: What's P(-1.96 < x < 1.96)?  ← the famous 95% rule
p = norm.cdf(1.96) - norm.cdf(-1.96)
print(f"P(-1.96 < x < 1.96) = {p:.3f}")                    # 0.950

# Q3: What x-value has 95% of area behind it? (inverse CDF)
x = norm.ppf(0.95, mean, std)
print(f"95th percentile = {x:.3f}")                         # 1.645

# In neural networks: weights initialized from N(0, 0.01) — this distribution