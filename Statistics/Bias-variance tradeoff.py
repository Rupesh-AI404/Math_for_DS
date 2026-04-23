import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import cross_val_score

np.random.seed(42)
X = np.sort(np.random.uniform(0, 1, 50)).reshape(-1, 1)
y = np.sin(2 * np.pi * X.ravel()) + np.random.normal(0, 0.2, 50)

for degree in [1, 3, 15]:
    model = Pipeline([
        ('poly', PolynomialFeatures(degree)),
        ('lr',   LinearRegression())
    ])
    # Cross-val score gives honest out-of-sample performance
    scores = cross_val_score(model, X, y, cv=5, scoring='neg_mean_squared_error')
    mse = -scores.mean()
    std = scores.std()
    label = {1: "underfit (high bias)", 3: "just right", 15: "overfit (high variance)"}
    print(f"Degree {degree:2d} [{label[degree]:25s}]: MSE={mse:.4f} ± {std:.4f}")

# Degree  1 [underfit (high bias)    ]: MSE=0.2800 ± 0.0312  ← too simple
# Degree  3 [just right              ]: MSE=0.0472 ± 0.0091  ← sweet spot
# Degree 15 [overfit (high variance) ]: MSE=0.2100 ± 0.1800  ← huge std = unstable