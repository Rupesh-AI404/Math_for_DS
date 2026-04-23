# python
from sklearn.model_selection import KFold, cross_val_score, LeaveOneOut, cross_val_predict
from sklearn.linear_model import Ridge
from sklearn.datasets import make_regression
from sklearn.metrics import r2_score
import numpy as np

X, y = make_regression(n_samples=100, n_features=5, noise=10, random_state=42)
model = Ridge(alpha=1.0)

# Option A: use a metric that is defined for single-sample test sets (LOO)
loo = LeaveOneOut()
scores_loo_mse = cross_val_score(model, X, y, cv=loo, scoring='neg_mean_squared_error')
print(f"LOO CV MSE (mean): {-scores_loo_mse.mean():.3f}")

# Option B: get LOO predictions for all samples and compute R^2 once
y_pred_loo = cross_val_predict(model, X, y, cv=loo)
print(f"LOO R^2 on full predictions: {r2_score(y, y_pred_loo):.3f}")
