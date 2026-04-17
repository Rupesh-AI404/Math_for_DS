import numpy as np
from numpy.linalg import inv

# This is the closed-form formula for linear regression
# b = (X^T · X)^-1 · X^T · y
# sklearn does this (or a numerically stable version) every time you call .fit()

X = np.array([[1, 2], [1, 3], [1, 4], [1, 5]])  # col of 1s + feature col
y = np.array([3, 5, 7, 9])

# The matrix math behind sklearn LinearRegression
b = inv(X.T @ X) @ X.T @ y
print("Intercept, slope:", b)   # [1.0, 2.0] ← exact solution

# Verify with sklearn — same answer
from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=False)
model.fit(X, y)
print("sklearn gives:", model.coef_)  # [1.0, 2.0] ← identical