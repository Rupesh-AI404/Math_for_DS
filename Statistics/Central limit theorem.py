import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

# Population that is completely NOT normal — it's uniform
population = np.random.exponential(scale=2, size=100_000)

# Take 1000 samples of size 35, compute each sample mean
sample_means = [np.mean(np.random.choice(population, 35)) for _ in range(1000)]

print(f"Population mean : {population.mean():.3f}")       # ~2.0
print(f"Sample means avg: {np.mean(sample_means):.3f}")   # ~2.0 ← same!
print(f"Shape of means  : approx normal despite skewed population")

# This justifies confidence intervals, t-tests, and hypothesis testing
# on ANY real-world data — even if the data itself isn't normal