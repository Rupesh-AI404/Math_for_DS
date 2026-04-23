import numpy as np
from scipy import stats

data = [12, 15, 14, 10, 18, 14, 900, 13, 16, 14]
#                                 ^^^^ outlier!

print(f"Mean   : {np.mean(data):.1f}")    # 102.0  ← destroyed by outlier
print(f"Median : {np.median(data):.1f}")  # 14.0   ← unaffected, use this
print(f"Mode   : {stats.mode(data).mode}") # 14    ← most frequent

# The lesson: salary data, house prices, any skewed data →
# always report median, not mean. This is why news uses median income.