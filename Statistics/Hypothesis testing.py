from scipy import stats
import numpy as np

# Did our new model improve accuracy?
# Old model scores: measured on 30 test runs
# New model scores: measured on 30 test runs
np.random.seed(42)
old_scores = np.random.normal(0.78, 0.04, 30)
new_scores = np.random.normal(0.82, 0.04, 30)

# Two-sample t-test
# H0: no difference between models (null hypothesis)
# H1: new model is different (alternative hypothesis)
t_stat, p_value = stats.ttest_ind(old_scores, new_scores)

print(f"t-statistic: {t_stat:.4f}")
print(f"p-value    : {p_value:.4f}")

if p_value < 0.05:
    print("Reject H0 — improvement is statistically significant")
else:
    print("Fail to reject H0 — difference could be random chance")

# p < 0.05 means: if there were NO real difference,
# we'd see results this extreme less than 5% of the time
# So we conclude the difference is real