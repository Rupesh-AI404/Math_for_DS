import numpy as np

# Hours studied vs exam score
hours = np.array([1, 2, 3, 4, 5, 6, 7, 8])
score = np.array([45, 50, 55, 65, 70, 75, 85, 90])

# Covariance — direction of relationship (but hard to interpret magnitude)
cov = np.cov(hours, score)[0, 1]
print(f"Covariance: {cov:.2f}")        # 30.0 (positive → move together)

# Pearson correlation — normalised to [-1, 1], easy to interpret
r = np.corrcoef(hours, score)[0, 1]
print(f"Correlation r: {r:.4f}")        # 0.9964 → very strong positive

# r² tells how much variance is explained
print(f"R-squared: {r**2:.4f}")         # 0.9928 → hours explains 99.3% of score variance

# In sklearn: use this BEFORE training to detect useless features
# r close to 0 → feature won't help prediction → drop it