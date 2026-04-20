import math

# Probability:  given a fair coin, what's the chance of 8 heads in 10?
# Likelihood:   given we SAW 8 heads in 10, how likely is p=0.5 vs p=0.8?

def binomial_likelihood(p, k, n):
    """How likely is parameter p, given we observed k successes in n trials"""
    from math import comb
    return comb(n, k) * (p**k) * ((1-p)**(n-k))

k, n = 8, 10   # observed: 8 heads in 10 flips

for p in [0.5, 0.7, 0.8, 0.9]:
    L = binomial_likelihood(p, k, n)
    print(f"  L(p={p} | 8/10 heads) = {L:.4f}")

# L(p=0.5) = 0.0439  ← fair coin is less likely
# L(p=0.8) = 0.3020  ← biased coin much more likely given data
# sklearn maximizes THIS when training any classifier