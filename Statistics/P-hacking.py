import numpy as np
from scipy import stats

np.random.seed(42)

# Simulate 100 completely random, meaningless features
# True relationship: NONE. All noise.
n_samples   = 50
n_features  = 100
X = np.random.randn(n_samples, n_features)
y = np.random.randn(n_samples)   # random target — no real relationship

# Test each feature for "significance"
false_discoveries = 0
for i in range(n_features):
    r, p = stats.pearsonr(X[:, i], y)
    if p < 0.05:
        false_discoveries += 1

print(f"Features tested   : {n_features}")
print(f"False discoveries : {false_discoveries}")
print(f"False positive rate: {false_discoveries/n_features:.1%}")

# Typically finds 3-6 "significant" features even though ALL are pure noise
# This is p-hacking — and it's what happens when you test many features
# Fix: Bonferroni correction — divide threshold by number of tests
corrected_threshold = 0.05 / n_features   # 0.0005
print(f"\nCorrected threshold: {corrected_threshold}")
