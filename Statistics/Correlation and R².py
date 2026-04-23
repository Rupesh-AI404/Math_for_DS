import numpy as np
from scipy import stats
from sklearn.metrics import r2_score

y_true = np.array([3, 5, 7, 9, 11, 13])
y_pred = np.array([2.8, 5.2, 6.9, 9.1, 10.8, 13.2])

# Pearson r: linear correlation between true and predicted
r, p_val = stats.pearsonr(y_true, y_pred)
print(f"Pearson r  : {r:.4f}  (p={p_val:.4f})")   # ~0.9998

# R²: proportion of variance explained by model
r2 = r2_score(y_true, y_pred)
print(f"R-squared  : {r2:.4f}")                    # ~0.9996

# Spearman r: rank correlation — use when relationship isn't linear
r_spear, p_spear = stats.spearmanr(y_true, y_pred)
print(f"Spearman r : {r_spear:.4f}")               # ~0.9998

# Interpretation:
# R² = 0.80 means model explains 80% of variance — 20% is unexplained noise
# R² < 0    means model is literally worse than just predicting the mean
# R² = 1.0  means perfect fit — usually means overfitting