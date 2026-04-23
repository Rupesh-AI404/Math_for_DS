import numpy as np
from scipy import stats

# Sample of 40 model accuracy scores from cross-validation
np.random.seed(42)
scores = np.random.normal(loc=0.82, scale=0.05, size=40)

mean   = scores.mean()
se     = stats.sem(scores)          # standard error = std / sqrt(n)
ci     = stats.t.interval(0.95, df=len(scores)-1, loc=mean, scale=se)

print(f"Sample mean      : {mean:.4f}")         # ~0.82
print(f"95% CI           : ({ci[0]:.4f}, {ci[1]:.4f})")
# "We are 95% confident the true accuracy is between 0.804 and 0.836"

# Wider CI = less data or more variance = less certain
# In practice: always report CI alongside model accuracy, not just the point estimate
# sklearn cross_val_score gives you the data to compute this directly