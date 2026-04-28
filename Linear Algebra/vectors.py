import numpy as np

# One customer record = one vector
customer = np.array([28, 55000, 3])  # age, income, purchases

# 1000 customers = a MATRIX of 1000 vectors
# This is exactly what X in sklearn.fit(X, y) looks like
X = np.array([
    [28, 55000, 3],
    [34, 72000, 7],
    [22, 38000, 1],
])
print(X.shape)  # (3, 3) → 3 samples, 3 features
print(X[0])
print(X[1])
print(X[3])
