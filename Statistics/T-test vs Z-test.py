from scipy import stats
import numpy as np

data = np.array([2.1, 2.5, 2.3, 2.8, 2.2, 2.6, 2.4])

# One-sample t-test: is this sample mean different from a known value?
# Use t-test when n < 30 OR population std is unknown (almost always)
t_stat, p_val = stats.ttest_1samp(data, popmean=2.0)
print(f"One-sample t-test: t={t_stat:.3f}, p={p_val:.4f}")

# Two-sample t-test: are two groups different?
group_a = np.array([85, 88, 90, 87, 92])
group_b = np.array([78, 82, 80, 79, 85])
t2, p2  = stats.ttest_ind(group_a, group_b)
print(f"Two-sample t-test: t={t2:.3f}, p={p2:.4f}")

# Paired t-test: same subjects, before vs after
before = np.array([70, 75, 68, 80, 72])
after  = np.array([75, 80, 74, 85, 78])
t3, p3 = stats.ttest_rel(before, after)
print(f"Paired t-test    : t={t3:.3f}, p={p3:.4f}")

# Rule of thumb:
# n >= 30 AND population std known → Z-test
# n <  30 OR  population std unknown → T-test (almost always use this)